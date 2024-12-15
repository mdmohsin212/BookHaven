from django.shortcuts import render, redirect
from author.models import *
from django.urls import reverse_lazy
from author.forms import RegisterForm
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView,LogoutView
from django.views.generic import FormView
from django.views import View
from books.models import BookModel
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
# Create your views here.

class UserRegistrationView(FormView):
    template_name = 'auth.html'
    form_class = RegisterForm
    success_url = reverse_lazy('profile')
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.get_form()
        context['type'] = 'Register'
        return context
    
class UserLoginView(LoginView):
    template_name = 'auth.html'
    model = AuthenticationForm
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type"] = 'Login' 
        return context
    
    def form_valid(self, form):
        messages.success(self.request, "Logged in Successfully")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.warning(self.request, "Incorrect login information")
        return super().form_invalid(form)
    
    def get_success_url(self):
        return reverse_lazy('profile')
    
@login_required
def UserProfile(request):
    books = BookModel.objects.filter(user=request.user)
    return render(request, 'profile.html', {'data' : books})

@method_decorator(login_required, name='dispatch')
class UserLogout(View):
    def get(self, request):
        logout(request)
        return redirect('login')
    