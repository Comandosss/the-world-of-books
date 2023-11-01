from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from catalog.models import Book, BookInstance, Author


def fetch_books_statistics():
    books = Book.objects.all()

    number_books = Book.objects.count()

    number_instances_available = (BookInstance.objects
                                  .filter(status__name='На складе')
                                  .count())

    number_authors = Author.objects.count()

    context = {
        'books': books,
        'number_books': number_books,
        'number_instances_available': number_instances_available,
        'number_authors': number_authors,
    }

    return context


def retrieve_book_detail_information(book_id):
    book = (Book.objects
            .prefetch_related('bookinstance_set__status')
            .get(pk=book_id))

    author_book = book.author.only('first_name', 'last_name')

    instances = book.bookinstance_set.all()

    context = {
        'book': book,
        'instances': instances,
        'author_book': author_book,
    }

    return context


def paginate(obj, page_number, items_per_page=3):
    paginator = Paginator(obj, items_per_page)
    try:
        page = paginator.page(page_number)
    except PageNotAnInteger:
        page = paginator.page(1)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)

    return page
