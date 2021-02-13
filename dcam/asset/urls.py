from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'devices', views.DeviceViewSet)

urlpatterns = [
    path('main/', views.index, name='index'),
    path('', include(router.urls)),
]
