from django.urls import path
from . import views

urlpatterns = [
    path('', views.CourseListAPIView.as_view(), name="Courses"),
    path('<int:id>', views.CourseDetailAPIView.as_view(), name="Courses")
]