from django.shortcuts import redirect, get_object_or_404
from django.views.generic import FormView
from django.urls import reverse_lazy
from transactions.forms import DepositeForm
from transactions.models import Wallet
from django.views import View
from books.models import BookModel
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# Create your views here.

@method_decorator(login_required, name='dispatch')
class Deposite(FormView):
    template_name = 'deposite.html'
    form_class = DepositeForm
    success_url = reverse_lazy('home')
    
    def form_valid(self, form):
        amount = form.cleaned_data.get('amount')
        if amount >= 100:
            wallet_balance,created=Wallet.objects.get_or_create(user=self.request.user)
            wallet_balance.balance+=amount
            wallet_balance.save()
            messages.success(self.request, f"Amount ${amount} deposited successfully.")
        else:
            messages.warning(self.request, 'Minimun Deposite amount 100$')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.get_form() 
        return context

@method_decorator(login_required, name='dispatch')
class BookBuy(View):
    def get(self, request, id):
        wallet,created=Wallet.objects.get_or_create(user=self.request.user)
        book = get_object_or_404(BookModel, pk=id)
        
        print(book.price)

        if book.price > wallet.balance:
            messages.error(request, 'You do not have enough money in your account. Add money.')
            return redirect('home')
        
        else:
            book.user.add(request.user)
            book.save()
            wallet.balance -= book.price
            wallet.save()
            return redirect('profile')

@method_decorator(login_required, name='dispatch')
class ReturnBook(View):
    def get(self, request, id):
        book = BookModel.objects.get(pk=id)
        book.user.remove(request.user)
        book.save()
        wallet=Wallet.objects.get(user=self.request.user)
        wallet.balance += book.price
        wallet.save()
        return redirect('profile')