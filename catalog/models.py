from django.db import models
import uuid #required for unique instances of objects

# Create your models here.

from django.urls import reverse # Used to generate URLs by reversing the URL patterns

class Account(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular account')
    accountName = models.CharField(max_length=30, help_text="Enter the name of the account holder")
    accountNumber = models.CharField(max_length=13, null=True)
    balance = models.CharField(max_length=22, null=True)
    address = models.CharField(max_length=100,null=True)
    phoneNumber = models.CharField(max_length=14, null=True)
    objects = models.Manager()

    def __str__(self):
        return self.accountName
    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('catalog:detail')

class Card(models.Model):
    """Model representing a specific ATM card."""
    # Foreign Key used because Card can only have one Account, but Account's can have multiple Cards
    account = models.ForeignKey('Account', on_delete=models.SET_NULL, null=True)
    pin = models.CharField( max_length=4)
    cardNumber = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique Id for this card', blank=True, editable=False)
    dateOfIssue = models.DateField(null=True, blank=True)
    expiryDate = models.DateField(null=True, blank=True)
    transactionHistory = models.ForeignKey('cardHistory', on_delete=models.SET_NULL, null=True);
    objects = models.Manager()

    CARD_STATUS = (
        ('m', 'Maintenance'),
        ('v', 'Valid'),
        ('e', 'Expired'),
        ('s', 'Lost/Stolen'),
        ('b', 'Blocked'),
    )

    status = models.CharField(
        max_length=1,
        choices=CARD_STATUS,
        blank=True,
        default='m',
        help_text='Card status',
    )


    def __str__(self):
        """String for representing the Model object."""
        return self.account.accountName

    def get_absolute_url(self):
        """Returns the url to access a detail record for this model."""
        return reverse('account-detail', args=[str(self.id)])

class ATM(models.Model):
    address = models.CharField(max_length=100,null=True)
    ATM_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'Opeartional'),
    )
    status = models.CharField(
        max_length=1,
        choices=ATM_STATUS,
        blank=True,
        default='m',
        help_text='Atm status'
    )

    lastRefillDate = models.DateField(null=True, blank=True)
    currentBalance = models.CharField(max_length=22, null=True)

class cardHistory(models.Model):
    history = models.TextField(max_length=22, null=True, default="History: ")

    def __str__(self):
        """String for representing the Model object."""
        return self.history

    def get_absolute_url(self):
        """Returns the url to access a detail record for this model."""
        return reverse('account-detail', args=[str(self.id)])
