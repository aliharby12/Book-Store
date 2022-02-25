from django import forms

from project.store.models import Address


class CheckoutForm(forms.ModelForm):
    """form for order checkout"""
    class Meta:
        model = Address
        exclude = ('user',)


class PaymentForm(forms.Form):
    stripeToken = forms.CharField(required=False)