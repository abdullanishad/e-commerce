import datetime
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


class OrderForm(forms.Form):
    # renewal_date = forms.DateField(help_text="Enter a date between now and 4 weeks (default 3).")
    pincode = forms.CharField(help_text="Enter pincode")
    address = forms.CharField(widget=forms.Textarea)
    # panchayath =  forms.IntegerField(label='pachayath/muncipality')

    STATUS = (
        ('kumbala', 'kumbala'),
        ('kasaragod', 'kasaragod'),
        ('puthur','puthur')
    )

    panchayath = forms.ChoiceField(choices=STATUS, label='pachayath/muncipality')

    phone_number = forms.IntegerField(help_text="Ex: 9876543210")


    def clean_pincode(self):
        data = self.cleaned_data['pincode']

        # Check if a date is not in the past.
        if data  != "671321" :
            raise ValidationError(_('Invalid pincode only deliverable to area under 671 321,121'))

        # Check if a date is in the allowed range (+4 weeks from today).
        # Remember to always return the cleaned data.
        return data
