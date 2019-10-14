from django.contrib import admin
from catalog.models import Account, Card

# Register your models here.
#admin.site.register(Account)
#admin.site.register(Card)
@admin.register(Account)



# Define the admin class
class AccountAdmin(admin.ModelAdmin):
    list_display = ('accountName', 'accountNumber', 'balance')

#when an admin class is registerd this way the class must be declared first. see registratioins for alternative.
#admin.site.register(Account, AccountAdmin)
@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ('account', 'dateOfIssue', 'expiryDate', 'cardNumber')
