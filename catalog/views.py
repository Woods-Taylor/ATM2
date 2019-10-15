from django.shortcuts import render
from catalog.models import Account as userAccount
from catalog.models import Card as userCard

# Create your views here.

def index(request):
    """View function for home page of site"""

    num_accounts = userAccount.objects.all().count()
    #num_cards = userCard.object.count()

    context = {
        'num_accounts' : num_accounts,
        #'num_cards' : num_cards,
        }

    return render(request, 'index.html', context=context)
