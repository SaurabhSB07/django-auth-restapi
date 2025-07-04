from django.urls import URLPattern,path
from .views import UserLoginView,UserRegistrationView,UserProfileView
from .views import UserChagePasswordResetEmailView,UserChangePasswordView



urlpatterns = [
    path('register/',UserRegistrationView.as_view(),name='regester'),
    path('login/',UserLoginView.as_view(),name='login'),
    path('profile/',UserProfileView.as_view(),name='profile'),
    path('changepassword/',UserChangePasswordView.as_view(),name='reset-password'),
    path('user-reset-pass-email/',UserChagePasswordResetEmailView.as_view(),name='user-reset-pass-email'),
    #path()
]