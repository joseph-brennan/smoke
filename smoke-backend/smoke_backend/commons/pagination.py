# -*- coding: utf-8 -*-

"""Simple helper to paginate query

Attributes:
    DEFAULT_PAGE_SIZE (int): The default amount of objects to put on a single
        page (50).

    DEFAULT_PAGE_NUMBER (int): The default beginning of the page sequence (1).

.. _Flask Pagination:
    http://flask.pocoo.org/snippets/44/
"""
from flask import url_for, request

DEFAULT_PAGE_SIZE = 50
DEFAULT_PAGE_NUMBER = 1


def paginate(query, schema):
    """A simple helper to paginate a query. [page]_

    Breaks apart a query returned by SQLAlchemy as defined through smoke's
    SQLAlchemy schema. [fsqlaquries]_ [fsqlaschema]_ The function returns the
    total number of pages, the current page a user is on, the next page object,
    the previous page object, and the results of the current page.

    Parameters:
        query (SQLAlchemy Query): The query to paginate. [fsqlaquries]_

        schema (Flask-SQLAlchemy Schema): The ORM schema which defines the
            objects in the database. [fsqlaschema]_

    Returns:
        JSON: Paginated view of the query passed in.
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
