from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from invoice.models import Invoice

from .serializers import InvoiceListSerializer, InvoiceCreateSerializer

class InvoiceListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'create':
            return InvoiceCreateSerializer
        return InvoiceListSerializer

    def get_queryset(self):
        user = self.request.user
        return Invoice.objects.filter(owner=user).select_related('client')
