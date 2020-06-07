import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from sadguru_api_app.models import Product
from sadguru_api_app.serializers import ProductSerializer


from rest_framework.test import RequestsClient
def test_get_productlist():
    client = RequestsClient()
    response =client.get('http://testserver/listapi/')
    assert response.status_code == 200

from django.urls import include, path, reverse
from rest_framework.test import APITestCase, URLPatternsTestCase
from sadguru_api_app import views
from sadguru_api_app.views import ProductDetail,ProductPost
from rest_framework.test import APIRequestFactory

"""URLPatternsTestCase,ProductList,ProductPost"""
class ProductTests(APITestCase, URLPatternsTestCase):
    urlpatterns = [
         path('listapi/',views.ProductList.as_view(),name='product-list'),
         path('detailapi/<int:pk>/',views.ProductDetail.as_view(),name='product-detail'),
         path('postapi/',views.ProductPost.as_view(),name='product-post'),
         path('deleteapi/<int:pk>/',views.ProductDelete.as_view(),name='product-delete'),
    ]

    def test_productlist(self):
        url = reverse('product-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        
    def test_productpost(self):
        url = reverse('product-post')
        data={"choice": "1", "name": "chaha","description":"limbu","price":16.0}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)

    def test_product_detail(self):
        factory = APIRequestFactory()
        view = ProductPost.as_view()
        request = factory.get('/detailapi/9')
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)