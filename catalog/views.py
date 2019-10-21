from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render
from catalog.models import Account as userAccount
from catalog.models import Card as userCard


# Create your views here.

def index(request):
    """View function for home page of site"""

    num_accounts = userAccount.objects.all().count()
    num_cards = userCard.objects.all().count()

    context = {
        'num_accounts' : num_accounts,
        'num_cards' : num_cards,
        }

    return render(request, 'index.html', context=context)

class AccountListView(generic.ListView):
    """Generic class-based view listing current user."""
    model = userAccount
    template_name ='catalog/Account_list_info_user.html'

    def get_queryset(self):
        return userAccount.balance
