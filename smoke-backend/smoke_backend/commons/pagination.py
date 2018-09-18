# -*- coding: utf-8 -*-

"""Simple helper to paginate query"""
from flask import url_for, request

DEFAULT_PAGE_SIZE = 50
DEFAULT_PAGE_NUMBER = 1

def paginate(query, schema):
    """Creates the first page
    
    Creates a next object that will contain data to the next page if there is another page
    Creates a previous object that will contain data to the previous page if there is a previous page
    Returns the total number of pages, the current page a user is on, the next object, 
    the previous object, and the results of the current page
    """
    page = request.args.get('page', DEFAULT_PAGE_NUMBER)
    per_page = request.args.get('page_size', DEFAULT_PAGE_SIZE)
    page_obj = query.paginate(page=page, per_page=per_page)

    
    next = url_for(
        request.endpoint,
        page=page_obj.next_num if page_obj.has_next else page_obj.page,
        per_page=per_page,
        **request.view_args
    )

    prev = url_for(
        request.endpoint,
        page=page_obj.prev_num if page_obj.has_prev else page_obj.page,
        per_page=per_page,
        **request.view_args
    )

    return {
        'total': page_obj.total,
        'pages': page_obj.pages,
        'next': next,
        'prev': prev,
        'results': schema.dump(page_obj.items).data
    }
