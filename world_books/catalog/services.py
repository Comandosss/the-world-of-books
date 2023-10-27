from catalog.models import Book, BookInstance, Author


def fetch_books_information_from_db():
    """Чтение из БД данных о книгах, их количестве в наличии
    и количестве авторов
    """

    text_head = 'На нашем сайте вы можете получить книги в электронном виде'

    books = Book.objects.all()
    number_books = Book.objects.count()

    number_instances_available = (BookInstance.objects
                                  .filter(status__name='На складе')
                                  .count())

    number_authors = Author.objects.count()

    context = {
        'text_head': text_head,
        'books': books,
        'number_books': number_books,
        'number_instances_available': number_instances_available,
        'number_authors': number_authors
    }

    return context
