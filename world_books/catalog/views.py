from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

from catalog.services import (fetch_books_statistics,
                              retrieve_book_detail_information)


def index(request: HttpRequest) -> HttpResponse:
    context = fetch_books_statistics()
    context.update({
        'text_head':
            'На нашем сайте вы можете получить книги в электронном виде',
        },
    )
    return render(request, 'catalog/index.html', context)


def books_list(request: HttpRequest) -> HttpResponse:
    context = fetch_books_statistics()
    return render(request, 'catalog/books_list.html', context)


def book_detail(request: HttpRequest, pk: int) -> HttpResponse:
    context = retrieve_book_detail_information(pk)
    return render(request, 'catalog/book_detail.html', context)
