from django.urls import path
from .views import RegisterView, VerifyEmail, LoginAPIView, UserListAPIView, UserDetailAPIView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('email-verify/', VerifyEmail.as_view(), name='email-verify'),
    path('users/', UserListAPIView.as_view(), name='users'),
    path('users/<int:id>', UserDetailAPIView.as_view(), name="users")
]