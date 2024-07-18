from .models import Products
from .serializers import ProductsSerializer
from rest_framework import generics,status
from rest_framework.response import Response


class ProductsListCreate(generics.ListCreateAPIView):
    queryset = Products.objects.all()
    serializer_class= ProductsSerializer

    def delete(self,request,*args,**kwargs):
        Products.objects.all.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)                                                            

class ProductsRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset=Products.objects.all()
    serializer_class= ProductsSerializer
    lookup_field="id"