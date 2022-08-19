from .serializers import *
from rest_framework import viewsets


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filterset_fields = '__all__'
    search_fields = ['date']

class Order_DetailViewSet(viewsets.ModelViewSet):
    queryset = Order_Detail.objects.all()
    serializer_class = Order_DetailSerializer
    filterset_fields = '__all__'
    search_fields = ['order']

