from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r"pings", views.PingView, 'ping')
router.register(r"logs", views.LogView, 'log')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]
