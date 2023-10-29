from catalog.models import Book, BookInstance, Author


def fetch_information_books_from_db():
    """Чтение из БД данных о книгах, их количестве в наличии
    и количестве авторов
    """

    books = Book.objects.only('title', 'price', 'photo')

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
