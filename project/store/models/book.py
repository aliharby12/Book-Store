from django.db import models

from project.store.models.abstracts import TimeStampedModel
from project.store.utils.image_save import PathAndRename


class Book(TimeStampedModel):
    """database table for books details"""
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to = PathAndRename('book/images/'))

    def __str__(self) -> str:
        return self.title