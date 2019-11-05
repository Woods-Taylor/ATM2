from django import forms

class getBalanceForm(forms.Form):
    accountNum = forms.CharField(help_text = "Enter your account number", label="Account Number")
    def clean_renewal_date(self):
        data = self.cleaned_data['accountNum']
        return data
