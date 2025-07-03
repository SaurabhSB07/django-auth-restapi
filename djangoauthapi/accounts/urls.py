from django.urls import URLPattern,path
from .views import UserLoginView
from .views import UserRegistrationView

urlpatterns = [
    path('register/',UserRegistrationView.as_view(),name='regester'),
    path('login/',UserLoginView.as_view(),name='login')
]