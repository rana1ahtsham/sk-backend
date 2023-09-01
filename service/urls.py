# yourapp/urls.py
from django.urls import path
from .views import ProviderView, NatureView, LocationView

urlpatterns = [
    path('nature/', NatureView.as_view(), name='service-nature'),
    path('location/', LocationView.as_view(), name='nature-location'),
    path('provider/', ProviderView.as_view(), name='nature-provider'),
]
