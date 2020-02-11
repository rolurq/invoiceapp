from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404
from django.template.loader import get_template
from django.contrib.auth.decorators import login_required

from xhtml2pdf import pisa

from .models import Invoice, ProductInvoice

@login_required
def generate_pdf(request, pk):
    user = request.user
    invoice = get_object_or_404(Invoice, pk=pk, owner=user)
    items = invoice.product_items
    partial_total = invoice.partial_total(items)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="invoice-%s.pdf"' % invoice.issue_date

    template = get_template('invoice.html')
    html = template.render({
        'invoice': invoice,
        'user': user,
        'items': items,
        'partial_total': partial_total,
        'total': partial_total + invoice.tax
    })

    status = pisa.CreatePDF(html, dest=response)
    if status.err:
        return HttpResponse('Error creating pdf', status=500)
    return response
