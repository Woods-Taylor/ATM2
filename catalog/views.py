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

def getAccountToView(request):
    '''form for account details'''
    return render(request, 'catalog/getAccountToView.html')

def getAccountToWithdrawal(request):
    '''form for account withdrawal'''
    return render(request, 'catalog/getAccountToWithdrawal.html')

def getAccountToTransfer(request):
    return render(request, 'catalog/getAccountToTransfer.html')

def details(request):
    card = get_object_or_404(userCard, pin = request.POST["text"])
    account = card.account
    return render(request, 'catalog/detail.html', {'account': account})

def transfer(request):
    card1 = get_object_or_404(userCard, pin = request.POST["yourpin"])
    card2 = get_object_or_404(userCard, pin = request.POST["theirpin"])
    amount = request.POST["amount"]
    account1 = card1.account
    account2 = card2.account
    account1.balance = int(account1.balance) - int(amount)
    account2.balance = int(account2.balance) + int(amount)
    account1.save()
    account2.save()
    return render(request, "catalog/success.html")

def withdraw(request):
    card = get_object_or_404(userCard, pin = request.POST["yourpin"])
    account = card.account
    account.balance = int(account.balance) - int(request.POST["amount"]) 
    account.save()
    return render(request, "catalog/detail.html", {"account" : account})
