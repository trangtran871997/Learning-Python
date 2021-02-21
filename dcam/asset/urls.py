from django.urls import path, include
from rest_framework import routers
from django_filters.views import FilterView
from . import views
from asset.models import Device

router = routers.DefaultRouter()
router.register(r'devices', views.DeviceViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path(r'changes/', views.get_changes)
]
