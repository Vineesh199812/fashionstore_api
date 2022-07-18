from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response

from products.models import products

class ProductView(APIView):
    def get(self,request,*args,**kwargs):
        return Response({"data":products})
    def post(self,request,*args,**kwargs):
        product=request.data
        products.append(product)
        return Response(data=product)

#url: store/products/{prid}
class ProductDetailsView(APIView):
    def get(self,request,*args,**kwargs):
        prid=kwargs.get("prid")
        product=[p for p in products if p["id"]==prid].pop()
        return Response(data=product)