from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from invoice.models import Invoice, Client, Product

from .serializers import InvoiceSerializer, ClientSerializer, ProductSerializer

class InvoiceListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = InvoiceSerializer

    def get_queryset(self):
        user = self.request.user
        return Invoice.objects.filter(owner=user).select_related('client')

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class ClientListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ClientSerializer

    def get_queryset(self):
        user = self.request.user
        return Client.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ProductListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProductSerializer

    def get_queryset(self):
        user = self.request.user
        return Product.objects.filter(owner=user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
