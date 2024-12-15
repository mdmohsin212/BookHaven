from django.urls import path
from books.views import BookDeatils


urlpatterns = [
    path('deatils/<int:id>/', BookDeatils.as_view(), name='book_deatils'),
]
