from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required

from project.store.models import Order, OrderItem, Book

@login_required
def increase_cart_item(request, pk):
    item = get_object_or_404(Book, pk=pk)
    order_item, created = OrderItem.objects.get_or_create(
        item=item, user=request.user
    )
    order_qs = Order.objects.filter(user=request.user, ordered=False).select_related('user')
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__pk=item.pk).exists():
            order_item.quantity += 1
            order_item.save()
            return redirect("cart-detail")
        else:
            order.items.add(order_item)
            return redirect("cart-detail")
    else:
        order = Order.objects.create(
            user=request.user)
        order.items.add(order_item)
        return redirect("cart-detail")


@login_required
def decrease_cart_item(request, pk):
    item = get_object_or_404(Book, pk=pk)
    order_qs = Order.objects.filter(user=request.user, ordered=False).select_related('user')
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__pk=item.pk).exists():
            order_item = OrderItem.objects.filter(item=item).select_related('item')[0]
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save(update_fields=['quantity'])
            else:
                order.items.remove(order_item)
            return redirect("cart-detail")
        else:
            return redirect("cart-detail")
    else:
        return redirect("cart-detail")


@login_required
def cart_detail(request):
    try:
        order = Order.objects.get(user=request.user, ordered=False)
        context = {
            'order': order
        }
        return render(request, 'cart.html', context)
    except:
        return render(request, 'cart.html')