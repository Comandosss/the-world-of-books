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


def retrieve_book_detail_information(pk):
    book = Book.objects.prefetch_related('bookinstance_set__status').get(pk=pk)

    author_book = book.author.only('first_name', 'last_name')

    instances = book.bookinstance_set.all()

    context = {
        'book': book,
        'instances': instances,
        'author_book': author_book,
    }

    return context
