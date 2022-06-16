from django.shortcuts import render
from .models import Products, ProductImages
from .serializers import ProductsSerializer
from django.http import JsonResponse, HttpResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, APIView




@api_view(['GET'])
def products_list(request):
    
    if request.method == 'GET':
        products = Products.objects.all()
        serializer = ProductsSerializer(products, context={'request': request}, many=True)
        return JsonResponse(serializer.data)


def product_details(request, pk):
    
    try:
        product = Products.objects.get(id=pk)
        print(product)
    except Products.DoesNotExist:
        return JsonResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProductsSerializer(product,context={'request': request})
        return JsonResponse(serializer.data)