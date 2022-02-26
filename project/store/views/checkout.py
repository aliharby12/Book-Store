from decimal import Decimal

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from project.store.forms import CheckoutForm
from project.store.models import Cart, Order, ORDER_STATUS, Address, Payment, OrderItem

import stripe, os

stripe.api_key = os.environ.get('STRIPE_SECRET_KEY')

@login_required
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


@login_required
def pay(request):
    """a view for paying"""
    if request.method == 'POST':
        try:
            address = Address.objects.filter(user=request.user).select_related('user').last()
            cart = Cart.objects.get(user=request.user)
            cart_items = cart.items.all()
            charge = stripe.PaymentIntent.create(
                amount=int(cart.get_cart_total() * 100),
                currency="usd",
                automatic_payment_methods={
                    'enabled': True,
                },
                description="charged from test account"
            )
            order = Order.objects.create(
                user=request.user,
                total=Decimal(cart.get_cart_total()),
                order_status=ORDER_STATUS.ORDERED,
                address=address
            )
            for cart_item in cart_items:
                order_item=OrderItem.objects.create(
                    item=cart_item.item,
                    quantity=cart_item.quantity,
                    user=request.user
                )
                order.items.add(order_item)
                cart_item.delete()
            cart.delete()

            # create the payment
            Payment.objects.create(
            stripe_charge_id = charge['id'],
            user = request.user,
            amount = order.total
            )
            messages.success(request, "Your order is created successfully!")
            return redirect("/")
        except:
            messages.warning(request, "something wrong!")
    return render(request, 'pay.html')