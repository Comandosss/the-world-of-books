from django.contrib import admin

from catalog.models import (Author, Book, Genre, Language,
                            Publisher, Status, BookInstance)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_birth', 'photo')
    fields = ['last_name', 'first_name', ('date_birth', 'photo')]


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'language', 'display_author')
    list_filter = ('genre', 'author')


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('book', 'status')
    fieldsets = (
        ('Экземпляр книги', {
            'fields': ('book', 'inventory_number'),
            },
        ),
        ('Статус и окончание его действия', {
            'fields': ('status', 'due_back'),
            },
        ),
    )

admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(Publisher)
admin.site.register(Status)
