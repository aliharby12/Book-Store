from django.test import TestCase

from project.store.models import Address, User

from model_bakery import baker


class TestAddressModel(TestCase):
    """basic test cases for address model"""

    def test_create_book(self):
        """test creating address"""
        address = Address.objects.create(
            city='Qena',
            street_1 = 'Street One',
            street_2 = 'Street Two',
            zip_code = '12345',
            user = baker.make(User)
        )
        self.assertEqual(address.city, 'Qena')

    def test_create_bulk_books(self):
        """test creating 1000 address"""
        addresses = baker.make(Address, _quantity=1000)
        self.assertEqual(len(addresses), 1000)