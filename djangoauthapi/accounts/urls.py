from django.urls import path
from .views import (
    UserLoginView,
    UserRegistrationView,
    UserProfileView,
    UserChagePasswordResetEmailView,
    UserChangePasswordView,
    UserPasswordResetView,
    
)

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),  
    path('login/', UserLoginView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('changepassword/', UserChangePasswordView.as_view(), name='change-password'),
    path('user-reset-pass-email/', UserChagePasswordResetEmailView.as_view(), name='user-reset-pass-email'),
    path('reset-password/<uid>/<token>/', UserPasswordResetView.as_view(), name='reset-password'),
]
