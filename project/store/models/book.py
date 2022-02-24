from django.db import models
from django.shortcuts import reverse

from project.store.models.abstracts import TimeStampedModel
from project.store.utils.image_save import PathAndRename


class Book(TimeStampedModel):
    """database table for books details"""
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to = PathAndRename('book/images/'))
    amount = models.IntegerField(default=0)

    def get_absolute_url(self):
        return reverse("book-detail", kwargs={
            'pk': self.pk
        })

    def get_increase_cart_item_url(self):
        return reverse("increase-cart-item", kwargs={
            'pk': self.pk
        })

    def get_decrease_cart_item_url(self):
        return reverse("decrease-cart-item", kwargs={
            'pk': self.pk
        })

    def __str__(self) -> str:
        return self.title