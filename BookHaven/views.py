from django.shortcuts import render
from django.views import View
from books.models import BookModel
from categories.models import Categorie

def Home(request, category_slug=None):
    data = BookModel.objects.all()
    catagory = Categorie.objects.all()
    
    if category_slug is not None:
        try:
            categories = Categorie.objects.get(slug=category_slug)
            data = BookModel.objects.filter(category=categories)
        except BookModel.DoesNotExist:
            data = Categorie.objects.none()
    
    return render(request, 'home.html', {'data': data, 'catagory' :catagory})