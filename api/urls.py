from django.urls import path, include

import rest_auth.urls
import rest_auth.registration.urls

urlpatterns = [
    path('auth/', include(rest_auth.urls)),
    path('auth/registration/', include(rest_auth.registration.urls)),
]