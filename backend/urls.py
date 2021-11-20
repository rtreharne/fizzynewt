from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
#from api import views
from rest_framework import permissions
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Fizzy Newt API",
      default_version='v1',
      description="Test description",
      terms_of_service="",
      contact=openapi.Contact(email="rob.treharne@gmail.com"),
      license=openapi.License(name="Test License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)



#router = routers.DefaultRouter()
#router.register(r"pings", views.PingView, 'ping')

urlpatterns = [
    #path('admin/', admin.site.urls),
    #path('api/', include(router.urls)),
    path('auth/', include('authentication.urls')),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui')
]
