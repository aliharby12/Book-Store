from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from project.store.models import Cart, OrderItem, Book

@login_required
def increase_cart_item(request, pk):
    item = get_object_or_404(Book, pk=pk)
    cart_item, created = OrderItem.objects.get_or_create(
        item=item, user=request.user
    )
    cart_qs = Cart.objects.filter(user=request.user).select_related('user')
    if cart_qs.exists():
        # check if the cart item is in the cart
        cart_qs = cart_qs[0]
        if cart_qs.items.filter(item__pk=item.pk).exists():
            cart_item.quantity += 1
            cart_item.save()
            messages.info(request, "This item quantity was updated.")
            return redirect("cart-detail")
        else:
            cart_qs.items.add(cart_item)
            messages.info(request, "This item was added to your cart.")
            return redirect("cart-detail")
    else:
        cart = Cart.objects.create(
            user=request.user)
        cart.items.add(cart_item)
        messages.info(request, "This item was added to your cart.")
        return redirect("cart-detail")


@login_required
def decrease_cart_item(request, pk):
    item = get_object_or_404(Book, pk=pk)
    cart_qs = Cart.objects.filter(user=request.user).select_related('user')
    if cart_qs.exists():
        # check if the cart item is in the cart
        cart_qs = cart_qs[0]
        if cart_qs.items.filter(item__pk=item.pk).exists():
            cart_item = OrderItem.objects.filter(item=item, user=request.user).select_related('item')[0]
            if cart_item.quantity > 1:
                cart_item.quantity -= 1
                cart_item.save(update_fields=['quantity'])
            else:
                cart_qs.items.remove(cart_item)
            messages.info(request, "This item quantity was updated.")
            return redirect("cart-detail")
        else:
            messages.info(request, "This item was not in your cart")
            return redirect("cart-detail")
    else:
        messages.info(request, "You do not have an active order")
        return redirect("cart-detail")


@login_required
def cart_detail(request):
    try:
        cart = Cart.objects.get(user=request.user)
        context = {
            'cart': cart
        }
        return render(request, 'cart.html', context)
    except:
        return render(request, 'cart.html')