from django.db import models

from project.store.models.abstracts import TimeStampedModel
from project.store.models import User, Book


class ORDER_STATUS(models.TextChoices):
    ORDERED = 'ORDERED', 'ORDERED'
    SHIPPING = 'SHIPPING', 'SHIPPING'
    DELIVERED = 'DELIVERED', 'DELIVERED'

class Order(TimeStampedModel):
    """database table for orders"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField('OrderItem')
    paied = models.BooleanField(default=False)
    total = models.DecimalField(max_digits=6, decimal_places=2)
    order_status = models.CharField(max_length=10, choices=ORDER_STATUS.choices, default=ORDER_STATUS.ORDERED)
    address = models.ForeignKey('Address', on_delete=models.DO_NOTHING)

    class Meta:
        constraints = [
            models.CheckConstraint(
                name="%(app_label)s_%(class)s_type_valid",
                check=models.Q(
                    order_status__in=ORDER_STATUS.values,
                ),
            )
        ]

    def __str__(self) -> str:
        return self.user.email


class OrderItem(TimeStampedModel):
    """database table for order items"""
    item = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def get_total_item_price(self):
        return self.quantity * self.item.price

    def __str__(self) -> str:
        return self.item.title


class Address(TimeStampedModel):
    """database model to store users address"""
    city = models.CharField(max_length=256)
    street_1 = models.CharField(max_length=256)
    street_2 = models.CharField(max_length=256, null=True, blank=True)
    zip_code = models.CharField(max_length=10)
    comment = models.TextField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.street_1


class Payment(models.Model):
    """database table to store payment info"""
    stripe_charge_id = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    amount = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return str(self.amount)