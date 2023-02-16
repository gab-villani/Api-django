
from django.contrib import admin
from django.urls import path,include
from app.views import CarroViewsSet
from rest_framework import routers 

router = routers.DefaultRouter()
router.register(r'carros',CarroViewsSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
]
