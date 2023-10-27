from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

from catalog.services import fetch_books_information_from_db


def index(request: HttpRequest) -> HttpResponse:
    context = fetch_books_information_from_db()
    return render(request, 'catalog/index.html', context)
