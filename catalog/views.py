from django.shortcuts import render
from catalog.models import Account as userAccount
from catalog.models import Card as userCard

from django.shortcuts import get_object_or_404

# Create your views here.

def index(request):
    """View function for home page of site"""

    num_accounts = userAccount.objects.all().count()
    count = 12857
    specific_account = userAccount._meta.fields

    num_cards = userCard.objects.all().count()

    context = {
        'num_accounts' : num_accounts,
        'specific_account' : specific_account,
        'num_cards' : num_cards,
        }

    return render(request, 'catalog/index.html', context=context)

def getAccount(request):
    '''form for account details'''
    return render(request, 'catalog/getAccount.html')

def details(request):
    card = get_object_or_404(userCard, pin = request.POST["text"])
    account = card.account
    return render(request, 'catalog/detail.html', {'account': account})


