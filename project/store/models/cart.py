from django.db import models

from project.store.models.abstracts import TimeStampedModel
from project.store.models import User, Book


class Cart(TimeStampedModel):
    """database table for cart"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    items = models.ManyToManyField('OrderItem')

    def get_cart_total(self):
        total = 0
        for cart_item in self.items.all():
            total += cart_item.get_total_item_price()
        return total

    def __str__(self) -> str:
        return self.user.email