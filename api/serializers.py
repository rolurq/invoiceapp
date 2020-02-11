from rest_framework import serializers

from invoice.models import Invoice, Client, ProductInvoice, Product

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        exclude = ('user',)
        read_only_fields = ('id',)

    def create(self, validated_data):
        client = Client(**validated_data)
        client.save()
        return client

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ('owner',)
        read_only_fields = ('id',)

    def create(self, validated_data):
        product = Product(**validated_data)
        product.save()
        return product

class ProductInvoiceSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(required=True, queryset=Product.objects.all())

    class Meta:
        model = ProductInvoice
        exclude = ('invoice',)
        read_only_fields = ('id',)

    def to_representation(self, instance):
        invoice = self.root.instance
        return {'product': instance.pk, 'invoice': invoice}

class InvoiceSerializer(serializers.ModelSerializer):
    client = serializers.PrimaryKeyRelatedField(required=True, queryset=Client.objects.all())
    items = ProductInvoiceSerializer(many=True, write_only=True)

    class Meta:
        model = Invoice
        exclude = ('owner',)
        read_only_fields = ('id', 'issue_date')

    def create(self, validated_data):
        items = validated_data.pop('items')
        invoice = Invoice(**validated_data)
        invoice.save()

        for item in items:
            ProductInvoice.objects.create(invoice=invoice, **item)
        return invoice
