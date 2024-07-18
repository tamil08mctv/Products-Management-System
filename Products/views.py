from .models import Products
from .serializers import ProductsSerializer
from rest_framework import generics, status
from rest_framework.response import Response

class ProductsListCreate(generics.ListCreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer

class ProductsRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    lookup_field = "id"

    def delete(self, request, *args, **kwargs):
        product_id = kwargs.get('id')
        try:
            product = Products.objects.get(id=product_id)
            product.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Products.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
