from posts.views import AddPostView
from django.urls import path
from .views import UserRegistration
from . import views

urlpatterns  = [
    path('Register/', UserRegistration.as_view(), name = 'Register'),
    
   
    
]