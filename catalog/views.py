from django.shortcuts import render
from catalog.models import Account as userAccount
from catalog.models import Card as userCard


# Create your views here.

def index(request):
    """View function for home page of site"""

    num_accounts = userAccount.objects.all().count()
    #test = "test"
    #count = 12857
    #specific_account = userAccount._meta.fields
    #accountId = userAccount.objects.get(id = )


    num_cards = userCard.objects.all().count()

    context = {
        'num_accounts' : num_accounts,
        #'specific_account' : specific_account,
        'num_cards' : num_cards,
        #'test' : test,
        }

    return render(request, 'index.html', context=context)
