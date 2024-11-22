from django.contrib import admin

from .models import Categoria, Author, Book

admin.site.register(Categoria)
admin.site.register(Author)
admin.site.register(Book)


