from django.urls import path
from . import views

urlpatterns = [
    path('', views.InstitutionListAPIView.as_view(), name="Institutions"),
    path('<int:id>', views.InstitutionDetailAPIView.as_view(), name="Institutions")
]