from django.contrib import admin
from book.models import Book, Author


# Register your models here.
@admin.register(Book)
class BookApp(admin.ModelAdmin):
    list_display = ['id', 'title']


@admin.register(Author)
class BookApp(admin.ModelAdmin):
    list_display = ['id', 'name']
