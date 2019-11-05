from django.shortcuts import render, get_object_or_404
from catalog.models import Account as userAccount
from catalog.models import Card as userCard


from django.http import HttpResponseRedirect
from django.urls import reverse

from catalog.forms import getBalanceForm
# Create your views here.

def index(request):
    """View function for home page of site"""

    num_accounts = userAccount.objects.all().count()
    test = "test"
    count = 12857
    specific_account = userAccount.objects.get(accountNumber='12345')
    num_cards = userCard.objects.all().count()

    context = {
        'num_accounts' : num_accounts,
        'specific_account' : specific_account,
        'num_cards' : num_cards,
        'test' : test,
        }

    return render(request, 'index.html', context=context)

def get_balance(request, pk):
    account = get_object_or_404(userAccount, pk=pk)


     # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = getBalanceForm(request.POST)
        account.save()

        return HttpResponseRedirect('/')
    else:
        basenum = 12345
        form = getBalanceForm(initial={'accountNum': basenum})

    context = {
        'form': form,
        'account': account,
    }

    return render(request, 'catalog/account_balance.html', context)
