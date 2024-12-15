from django.shortcuts import render
from django.views.generic import DetailView
from books.models import BookModel, Comment
from books.forms import *
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# Create your views here.

class BookDeatils(DetailView):
    model = BookModel
    template_name = 'book_deatils.html'
    pk_url_kwarg = 'id'
    context_object_name = 'data'
    
    @method_decorator(login_required, name='dispatch')
    def post(self, request, *args, **kwargs):   
        form = CommentForm(data=self.request.POST)
        data = self.get_object()
        if form.is_valid():
            comment = form.save(commit=False)
            comment.book = data
            comment.save()
        return self.get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        comment = Comment.objects.filter(book=self.object)
        comment_form = CommentForm()
        context["comments"] = comment
        context["form"] = comment_form
        return context  