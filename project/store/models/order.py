from django.db import models

from project.store.models.abstracts import TimeStampedModel
from project.store.models import User


class ORDER_STATUS(models.TextChoices):
    ORDERED = 'ORDERED', 'ORDERED'
    SHIPPING = 'SHIPPING', 'SHIPPING'
    DELIVERED = 'DELIVERED', 'DELIVERED'

class Order(TimeStampedModel):
    """database table for orders"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField('CartItem')
    address_detail = models.TextField()
    paied = models.BooleanField(default=False)
    total = models.DecimalField(max_digits=6, decimal_places=2)
    order_status = models.CharField(max_length=10, choices=ORDER_STATUS.choices, default=ORDER_STATUS.ORDERED)

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