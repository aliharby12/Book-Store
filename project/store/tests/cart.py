from django.test import TestCase

from project.store.models import Cart, OrderItem, Book, User

from model_bakery import baker


class TestCartModel(TestCase):
    """basic test cases for book model"""

    def setUp(self):
        """create an order item instance"""

        self.order_item = OrderItem.objects.create(
            item=baker.make(Book),
            quantity=10,
            user=baker.make(User)
        )

    def test_create_user_cart(self):
        """test creating user cart"""
        cart = Cart.objects.create(
            user=baker.make(User)
        )
        cart.items.set([self.order_item])
        self.assertEqual(cart.items.count(), 1)