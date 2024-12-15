from django.contrib import admin
from books.models import BookModel, Comment

# Register your models here.

admin.site.register(BookModel)
admin.site.register(Comment)