# -*- coding: utf-8 -*-

"""Simple helper to paginate query.
"""
from flask import url_for, request

DEFAULT_PAGE_SIZE = 50
DEFAULT_PAGE_NUMBER = 1

def paginate(query, schema):
    """A simple helper to paginate a query.

    This function will take a query and schema and separate the query results into pages with 50 entries per page.
    It will also create links to the next and previous result pages as objects called next and previous.
    The function returns the total number of pages, the current page a user is on, the next page object, the previous
    page object, and the results of the current page.
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
