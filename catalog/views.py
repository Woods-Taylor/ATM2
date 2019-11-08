from django.shortcuts import render
from catalog.models import Account as userAccount
from catalog.models import Card as userCard

from django.shortcuts import get_object_or_404

# Create your views here.

def index(request):
    """View function for home page of site"""
    num_accounts = userAccount.objects.all().count()
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
    if int(account1.balance) - int(amount) > 0:
        account2 = card2.account
        prevBal = account1.balance
        account1.balance = int(account1.balance) - int(amount)
        account2.balance = int(account2.balance) + int(amount)
        account1.save()
        account2.save()
        return render(request, "catalog/success.html", {'account': account1, 
                                                        'prevBal':prevBal,
        })
    return render(request, "catalog/failure.html")

def withdraw(request):
    card = get_object_or_404(userCard, pin = request.POST["yourpin"])
    account = card.account
    if int(account.balance) - int(request.POST["amount"]) > 0:
        prevBal = account.balance
        account.balance = int(account.balance) - int(request.POST["amount"]) 
        account.save()
        return render(request, "catalog/success.html", {"account" : account,
                                                        "prevBal" : prevBal
        })
    return render(request, "catalog/failure.html")