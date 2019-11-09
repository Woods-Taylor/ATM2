from django.shortcuts import render
from catalog.models import Account as userAccount
from catalog.models import Card as userCard
from catalog.models import ATM

from django.shortcuts import get_object_or_404

# Create your views here.
def index(request):
    """View function for home page of site"""
    num_accounts = userAccount.objects.all().count()
    specific_account = userAccount._meta.fields
    num_cards = userCard.objects.all().count()
    atm = get_object_or_404(ATM, address = "14way")

    context = {
        'num_accounts' : num_accounts,
        'specific_account' : specific_account,
        'num_cards' : num_cards,
        'atm': atm,
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
    atm = get_object_or_404(ATM, address = "14way")
    amount = request.POST["amount"]
    account1 = card1.account

    if card1.status != 'v':
        return render(request, "catalog/failure.html", {"message": "Card not vaild"})

    if int(account1.balance) - int(amount) > 0 and int(atm.currentBalance) - int(amount) > 0:
        account2 = card2.account
        prevBal = account1.balance
        account1.balance = int(account1.balance) - int(amount)
        account2.balance = int(account2.balance) + int(amount)
        account1.save()
        account2.save()
        atm.currentBalance = int(atm.currentBalance) - int(amount)
        atm.save()
        return render(request, "catalog/success.html", {'account': account1, 
                                                        'prevBal':prevBal,
        })
    elif int(account1.balance) - int(amount) <= 0:
        return render(request, "catalog/failure.html", {"message":"insufficent funds in banking account!"})
    elif int(atm.currentBalance) - int(amount) <= 0:
        return render(request, "catalog/failure.html", {"message":"insufficent funds in ATM!"})
    return render(request, "catalog/failure.html", {"message":"error not cataloged"})

def withdraw(request):
    card = get_object_or_404(userCard, pin = request.POST["yourpin"])
    atm = get_object_or_404(ATM, address = "14way")
    account = card.account
    amount = request.POST["amount"]
    if int(account.balance) - int(amount) > 0 and int(atm.currentBalance) - int(amount) > 0:
        prevBal = account.balance
        account.balance = int(account.balance) - int(amount) 
        account.save()
        atm.currentBalance = int(atm.currentBalance) - int(amount)
        atm.save()
        return render(request, "catalog/success.html", {"account" : account,
                                                        "prevBal" : prevBal
        })
    elif int(account.balance) - int(amount) <= 0:
        return render(request, "catalog/failure.html", {"message":"insufficent funds in banking account!"})
    elif int(atm.currentBalance) - int(amount) <= 0:
        return render(request, "catalog/failure.html", {"message":"insufficent funds in ATM!"})
    return render(request, "catalog/failure.html", {"message":"error not cataloged!"})