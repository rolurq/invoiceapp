from django.db import models

from user.models import User

class Client(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)

    class Meta:
        unique_together = ('user', 'name')

class Product(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=250)
    price = models.FloatField()

    class Meta:
        unique_together = ('owner', 'name')

class Invoice(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    items = models.ManyToManyField(Product, through='ProductInvoice')
    issue_date = models.DateField(auto_now_add=True)
    terms = models.TextField()
    tax = models.FloatField()

    @property
    def product_items(self):
        return ProductInvoice.objects.filter(invoice=self).annotate(
            amount=models.ExpressionWrapper(
                models.F('quantity') * models.F('product__price'),
                output_field=models.FloatField()))

    def partial_total(self, items=None):
        resolved_items = self.product_items if items is None else items
        return resolved_items.aggregate(
            models.Sum('amount', output_field=models.FloatField())).get('amount__sum')

class ProductInvoice(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
