from django.urls import path
from . import views

urlpatterns = [
    path('', views.SchoolListAPIView.as_view(), name="schools"),
    path('<int:id>', views.SchoolDetailAPIView.as_view(), name="schools")
]