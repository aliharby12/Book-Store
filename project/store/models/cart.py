from django.db import models

from project.store.models.abstracts import TimeStampedModel
from project.store.models import User, Book


class Cart(TimeStampedModel):
    """database table for cart"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    items = models.ManyToManyField('CartItem')

    def get_cart_total(self):
        total = 0
        for cart_item in self.items.all():
            total += cart_item.get_total_item_price()
        return total

    def __str__(self) -> str:
        return self.user.email


class CartItem(TimeStampedModel):
    """database table for cart items"""
    item = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    
    def get_total_item_price(self):
        return self.quantity * self.item.price

    def __str__(self) -> str:
        return self.item.title