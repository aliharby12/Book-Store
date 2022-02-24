from django import forms

from project.store.models import Order


class CheckoutForm(forms.ModelForm):
    """form for order checkout"""
    class Meta:
        model = Order
        fields = ('address_detail',)