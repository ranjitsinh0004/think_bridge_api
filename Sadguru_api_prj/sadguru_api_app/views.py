from sadguru_api_app.models import Product
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from sadguru_api_app.serializers import ProductSerializer
from django.shortcuts import redirect
from rest_framework import status
from django.views.generic import View
import json
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render
#from rest_framework.decorators import api_view



class ProductList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'product_list.html'
    
    
    def get(self, request):
        queryset = Product.objects.all()
        return Response({'product': queryset})


class ProductDetail(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'product_detail.html'

    #@api_view(['GET',])
    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        serializer = ProductSerializer(product)
        return Response({'serializer': serializer, 'product': product})

    #@api_view(['POST'])
    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        serializer = ProductSerializer(product, data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'product': product})
        serializer.save()
        return redirect('product-list')


class ProductPost(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'product_post.html'

    def get(self, request):
        serializer = ProductSerializer()
        return Response({'serializer': serializer,})

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer,})
        serializer.save()
        return redirect('product-list')

'''class ProductDelete(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'product_delete.html'
    
    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        serializer = ProductSerializer(product)
        return Response({'serializer': serializer, 'product': product})
    def delete(self,request, pk,*args,**kwargs):
        data=self.request.body
        #print('data: --->',data)
        return Response({'msg': 'response from delete method',})'''

class ProductDelete(DeleteView):
    model = Product
    template_name = 'product_delete.html'
    success_url = reverse_lazy('product-list')



