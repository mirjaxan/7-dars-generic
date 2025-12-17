from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin,DestroyModelMixin,UpdateModelMixin,RetrieveModelMixin,ListModelMixin
from rest_framework.response import Response
from rest_framework import status

from .models import Product,Author
from .serializers import ProductSerializer,AuthorSerializer



class ProductAPIView(GenericAPIView,CreateModelMixin,ListModelMixin):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)
    
class ProductDetailDestroyUpdateAPIView(GenericAPIView,DestroyModelMixin,UpdateModelMixin,RetrieveModelMixin):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)
    
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    
    def patch(self,request,*args,**kwargs):
        return self.partial_update(request,*args,**kwargs)
    
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)
    


    

class AuthorAPIView(GenericAPIView,CreateModelMixin,ListModelMixin):
    queryset = Author.objects.all()
    serializer_class = ProductSerializer

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)
    
class AuthorDetailDestroyUpdateAPIView(GenericAPIView,CreateModelMixin,ListModelMixin,DestroyModelMixin,RetrieveModelMixin):
    
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def get(self,request,*args,**kwargs):
        return self.retrive(request,*args,**kwargs)
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    def patch(self,request,*args,**kwargs):
        return self.partial_update(request,*args,**kwargs)
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)