from django.contrib import admin
from catalog.models import Account, Card, ATM, cardHistory

# Register your models here.
#admin.site.register(Account)
#admin.site.register(Card)
@admin.register(Account)
# Define the admin class
class AccountAdmin(admin.ModelAdmin):
    list_display = ('accountName', 'accountNumber', 'balance',)

#when an admin class is registerd this way the class must be declared first. see registratioins for alternative.
#admin.site.register(Account, AccountAdmin)
@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ('account', 'dateOfIssue', 'expiryDate', 'cardNumber', 'transactionHistory')

@admin.register(ATM)
class ATMAdmin(admin.ModelAdmin):
    list_display = ('address', 'lastRefillDate', 'currentBalance')

@admin.register(cardHistory)
class cardHistory(admin.ModelAdmin):
    list_display = ['history']
