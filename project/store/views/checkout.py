from django.shortcuts import render, redirect

from project.store.forms import CheckoutForm
from project.store.models import Order


def checkout(request):
    """a view for checkout process"""
    order = Order.objects.get(user=request.user, ordered=False)
    form = CheckoutForm()
    print(12)
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            order.address_detail = request.POST.get('address_detail')
            order.save(update_fields=['address_detail'])
            return redirect('pay')
    context = {'form':form}
    return render(request, 'checkout.html', context)


def pay(request):
    """a view for paying"""
    return render(request, 'pay.html')