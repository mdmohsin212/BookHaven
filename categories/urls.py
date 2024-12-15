from django.urls import path
from author.views import *


urlpatterns = [
    path('login/', UserRegistrationView.as_view()),
]
