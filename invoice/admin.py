from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse

from user.admin import public_admin

from .models import *

admin.site.register(Invoice)
admin.site.register(Product)
admin.site.register(Client)

class ProductInvoiceInline(admin.TabularInline):
    model = ProductInvoice
    extra = 1

    def has_add_permission(self, request):
        return True

    def has_change_permission(self, request, obj=None):
        if obj is None:
            return False;
        return request.user == obj.owner
    
    def has_delete_permission(self, request, obj=None):
        return self.has_change_permission(request, obj)

    def has_module_permission(self, request):
        return True

    def get_field_queryset(self, db, db_field, request):
        if db_field.name == 'product':
            return db_field.remote_field.model.objects.filter(owner=request.user)
        return super().get_field_queryset(db, db_field, request)

class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('issue_date', 'client', 'pdf')
    list_select_related = ('client',)
    inlines = (ProductInvoiceInline,)

    def pdf(self, obj):
        return format_html('<a href="{}" class="button">Download</a>', reverse('invoice-pdf', args=(obj.pk,)))
    pdf.allow_tags = True
    pdf.short_description = "Download pdf"

    def get_field_queryset(self, db, db_field, request):
        if db_field.name == 'owner':
            return db_field.remote_field.model.objects.filter(pk=request.user.pk)
        elif db_field.name == 'client':
            return db_field.remote_field.model.objects.filter(user=request.user)
        return super().get_field_queryset(db, db_field, request)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(owner=request.user)

    def has_add_permission(self, request):
        return True

    def has_change_permission(self, request, obj=None):
        if obj is None:
            return False;
        return request.user == obj.owner
    
    def has_delete_permission(self, request, obj=None):
        return self.has_change_permission(request, obj)

    def has_module_permission(self, request):
        return True

class ClientAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(user=request.user)

    def has_add_permission(self, request):
        return True

    def has_change_permission(self, request, obj=None):
        if obj is None:
            return False;
        return request.user == obj.user
    
    def has_delete_permission(self, request, obj=None):
        return self.has_change_permission(request, obj)

    def has_module_permission(self, request):
        return True

class ProductAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(owner=request.user)

    def has_add_permission(self, request):
        return True

    def has_change_permission(self, request, obj=None):
        if obj is None:
            return False;
        return request.user == obj.owner
    
    def has_delete_permission(self, request, obj=None):
        return self.has_change_permission(request, obj)

    def has_module_permission(self, request):
        return True

public_admin.register(Invoice, InvoiceAdmin)
public_admin.register(Client, ClientAdmin)
public_admin.register(Product, ProductAdmin)
