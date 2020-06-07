from django.test import TestCase
from sadguru_api_app.models import Product


class ProductTest(TestCase):
    """ Test module for Product model """

    def setUp(self):
        Product.objects.create(
            choice='1', name='chaha', description='Fakkad', price=15)
        Product.objects.create(
            choice='2', name='pohe', description='Kanda', price=20)

    def test_product(self):
        product_chaha = Product.objects.get(name='chaha')
        product_pohe = Product.objects.get(name='pohe')
        self.assertEqual(
            product_chaha.__str__(), "chaha")
        self.assertEqual(
            product_pohe.__str__(), "pohe")

