from decimal import Decimal
from django.shortcuts import render, redirect
from django.contrib import messages

from project.store.forms import CheckoutForm, PaymentForm
from project.store.models import Cart, Order, ORDER_STATUS, Address, Payment

import stripe, os

stripe.api_key = os.environ.get('STRIPE_SECRET_KEY')


def checkout(request):
    """a view for checkout process"""
    form = CheckoutForm()    
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            address = form.save(commit=False)
            address.user = request.user
            address.save()
            return redirect('pay')
    context = {'form':form}
    return render(request, 'checkout.html', context)


def pay(request):
    """a view for paying"""
    if request.method == 'POST':
        address = Address.objects.filter(user=request.user).select_related('user').last()
        cart = Cart.objects.get(user=request.user)
        cart_items = cart.items.all()
        form = PaymentForm(request.POST)
        if form.is_valid():
            charge = stripe.Charge.create(
                amount=int(cart.get_cart_total() * 100),
                currency="usd",
                source=form.cleaned_data.get('stripeToken')
            )
            order = Order.objects.create(
                user=request.user,
                total=Decimal(cart.get_cart_total()),
                order_status=ORDER_STATUS.ORDERED,
                address=address
            )
            order.items.add(*cart_items)
            cart.delete()

            # create the payment
            Payment.objects.create(
            stripe_charge_id = charge['id'],
            user = request.user,
            amount = order.get_total()
            )
            messages.success(request, "Your order was successful!")
            return redirect("/")
    else:
        form = PaymentForm()
    return render(request, 'pay.html')