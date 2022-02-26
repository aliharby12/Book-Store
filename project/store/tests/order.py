from django.test import TestCase

from project.store.models import Book, Address, Order, User, OrderItem, ORDER_STATUS

from model_bakery import baker



class TestOrderModel(TestCase):
    """basic test cases for book model"""

    def setUp(self):
        """create an order and order item instance"""

        self.order_item = OrderItem.objects.create(
            item=baker.make(Book),
            quantity=10,
            user=baker.make(User)
        )

    def test_create_order(self):
        """test creating order"""
        order = Order.objects.create(
            user=baker.make(User),
            order_status=ORDER_STATUS.ORDERED,
            address=baker.make(Address),
            total=100
        )
        order.items.set([self.order_item])
        self.assertEqual(order.items.count(), 1)

    def test_create_order_item(self):
        """test create order item"""
        self.assertEqual(self.order_item.quantity, 10)