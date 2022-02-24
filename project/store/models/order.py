from django.db import models

from project.store.models.abstracts import TimeStampedModel
from project.store.models import User, Book


class Order(TimeStampedModel):
    """database table for orders"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField('OrderItem')
    address_detail = models.TextField()
    delivered = models.BooleanField(default=False)
    ordered = models.BooleanField(default=False)
    paied = models.BooleanField(default=False)

    def get_total(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_total_item_price()

        return total

    def __str__(self) -> str:
        return self.user.email


class OrderItem(TimeStampedModel):
    """database table for order items"""
    item = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def get_total_item_price(self):
        return self.quantity * self.item.price

    def __str__(self) -> str:
        return self.item.title