from django.contrib import admin

from catalog.models import (Author, Book, Genre, Language,
                            Publisher, Status, BookInstance)
from django.utils.html import format_html


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_birth',
                    'photo', 'show_picture')
    fields = ['last_name', 'first_name', ('date_birth', 'photo')]
    readonly_fields = ['show_picture']

    def show_picture(self, obj):
        return format_html(
            f'<img src="{obj.photo.url}" style="max-height: 100px;">')

    show_picture.short_description = 'Фото'


class BookInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 1


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'language',
                    'show_authors', 'show_picture')
    list_filter = ('genre', 'author')
    inlines = [BookInstanceInline]
    readonly_fields = ['show_picture']

    def show_picture(self, obj):
        return format_html(
            f'<img src="{obj.photo.url}" style="max-height: 100px;">')

    show_picture.short_description = 'Обложка'


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('book', 'status')
    fieldsets = (
        (
            'Экземпляр книги', {
                'fields': ('book', 'inventory_number'),
            },
        ),
        (
            'Статус и окончание его действия', {
                'fields': ('status', 'due_back'),
            },
        ),
    )


admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(Publisher)
admin.site.register(Status)
