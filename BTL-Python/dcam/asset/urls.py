from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'devices', views.DeviceViewSet)

urlpatterns = [
    path('index/', views.index, name='index'),
    path('main/', views.main, name='main'),
    path('logout/', views.customized_logout, name='logout'),
    path('', include(router.urls)),
]
