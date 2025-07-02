from django.urls import URLPattern,path
from .views import UserRegistrationView

urlpatterns = [
    path('register/',UserRegistrationView.as_view(),name='regester'),
]