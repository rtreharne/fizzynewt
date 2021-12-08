from django.urls import path
from . import views

urlpatterns = [
    path('', views.EnrollmentListAPIView.as_view(), name="enrollment"),
    path('<int:id>', views.EnrollmentDetailAPIView.as_view(), name="enrollment")
    #path('<int:id>', views.EnrollmentDetailAPIView(), name="enrollment"),
]