from django.views.generic import RedirectView
from .views import DashboardView, MapView
from django.urls import path

urlpatterns = [
    path('', RedirectView.as_view(url='/dashboard/')),
    path('dashboard/', DashboardView.as_view(), name='dashboard_view'),
    path('map/', MapView.as_view(), name='map_view'),
]