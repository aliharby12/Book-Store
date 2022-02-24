from decimal import Decimal
from django.shortcuts import render, redirect

from project.store.forms import CheckoutForm
from project.store.models import Cart, Order, ORDER_STATUS


def checkout(request):
    """a view for checkout process"""
    form = CheckoutForm()
    cart = Cart.objects.get(user=request.user)
    cart_items = cart.items.all()
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            order = Order.objects.create(
                user=request.user,
                address_detail=request.POST.get('address_detail'),
                total=Decimal(cart.get_cart_total()),
                order_status=ORDER_STATUS.ORDERED
            )
            order.items.add(*cart_items)
            return redirect('pay')
    context = {'form':form}
    return render(request, 'checkout.html', context)


def pay(request):
    """a view for paying"""
    return render(request, 'pay.html')