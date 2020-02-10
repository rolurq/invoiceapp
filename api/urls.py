from django.urls import path, include

import rest_auth.urls
import rest_auth.registration.urls

from .views import InvoiceListCreateView

urlpatterns = [
    path('auth/', include(rest_auth.urls)),
    path('auth/registration/', include(rest_auth.registration.urls)),
    path('invoice/', InvoiceListCreateView.as_view())
]