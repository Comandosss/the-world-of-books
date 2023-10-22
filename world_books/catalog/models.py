from django.db import models
from django.urls import reverse


class Genre(models.Model):
    name = models.CharField(
        max_length=200,
        help_text='Введите жанр книги',
        verbose_name='Жанр книги'
    )

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(
        max_length=20,
        help_text='Введите язык книги',
        verbose_name='Язык книги'
    )

    def __str__(self):
        return self.name


class Pusblisher(models.Model):
    name = models.CharField(
        max_length=20,
        help_text='Введите наименование издательства',
        verbose_name='Издательство'
    )

    def __str__(self):
        return self.name


class Author(models.Model):
    first_name = models.CharField(
        max_length=100,
        help_text='Введите имя',
        verbose_name='Имя автора'
    )
    last_name = models.CharField(
        max_length=100,
        help_text='Введите фамилию',
        verbose_name='Фамилия автора'
    )
    date_birth = models.DateField(
        help_text='Введите дату рождения',
        verbose_name='Дата рождения',
        null=True,
        blank=True
    )
    about = models.TextField(
        help_text='Введите сведения об авторе',
        verbose_name='Сведения об авторе'
    )
    photo = models.ImageField(
        upload_to='images',
        help_text='Загрузите фото автора',
        verbose_name='Фото автора',
        null=True,
        blank=True
    )

    def __str__(self):
        return self.last_name


class Book(models.Model):
    title = models.CharField(
        max_length=200,
        help_text='Введите название книги',
        verbose_name='Название книги'
    )
    genre = models.ForeignKey(
        'Genre',
        on_delete=models.CASCADE,
        help_text='Выберите жанр для книги',
        verbose_name='Жанр книги',
        null=True
    )
    language = models.ForeignKey(
        'Language',
        on_delete=models.CASCADE,
        help_text='Выберите язык книги',
        verbose_name='Язык книги',
        null=True
    )
    pusblisher = models.ForeignKey(
        'Pusblisher',
        on_delete=models.CASCADE,
        help_text='Выберите издательство',
        verbose_name='Издательство',
        null=True
    )
    year = models.CharField(
        max_length=4,
        help_text='Введите год издания',
        verbose_name='Год издания'
    )
    author = models.ManyToManyField(
        'Author',
        help_text='Выберите автора (авторов) книги',
        verbose_name='Автор (авторы) книги')
    summary = models.TextField(
        max_length=1000,
        help_text='Введите краткое описание книги',
        verbose_name='Аннотация книги'
    )
    isbn = models.CharField(
        max_length=4,
        help_text='Должно содержать 13 символов',
        verbose_name='ISBN книги'
    )
    price = models.DecimalField(
        max_length=4,
        help_text='Введите цену книги',
        verbose_name='Цена (руб.)'
    )
    photo = models.ImageField(
        upload_to='images',
        help_text='Загрузите изображение обложки',
        verbose_name='Изображение обложки'
    )

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])
