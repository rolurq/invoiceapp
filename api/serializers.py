from rest_framework import serializers

from invoice.models import Invoice, Client, ProductInvoice, Product

class InvoiceClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('name',)

class InvoiceListSerializer(serializers.ModelSerializer):
    client = InvoiceClientSerializer(read_only=True)

    class Meta:
        model = Invoice
        fields = ('id', 'issue_date', 'client')

class InvoiceCreateClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('name', 'address', 'city', 'state', 'country', 'zip_code',)

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'description', 'price')

class ProductInvoiceSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = ProductInvoice
        fields = ('quantity', 'product')

class InvoiceCreateSerializer(serializers.ModelSerializer):
    client = InvoiceCreateClientSerializer()
    items = ProductInvoiceSerializer(many=True)

    class Meta:
        model = Invoice
        fields = ('terms', 'tax', 'client', 'items')
