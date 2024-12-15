from django.urls import path
from transactions.views import *


urlpatterns = [
    path('deposite/', Deposite.as_view(), name='deposite'),
    path('buy/<int:id>/', BookBuy.as_view(), name='Buy'),
    path('return/<int:id>/', ReturnBook.as_view(), name='Return'),
]
