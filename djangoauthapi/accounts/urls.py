from django.urls import URLPattern,path
from .views import UserLoginView
from .views import UserRegistrationView
from .views import UserProfileView


urlpatterns = [
    path('register/',UserRegistrationView.as_view(),name='regester'),
    path('login/',UserLoginView.as_view(),name='login'),
    path('profile/',UserProfileView.as_view(),name='profile')
]