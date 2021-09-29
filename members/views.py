from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from django.views.generic import CreateView
from django.urls import reverse_lazy

# Create your views here.
class UserRegistration(generic.CreateView):
    form_class  = UserCreationForm
    template_name = 'registration.html'
    success_url = reverse_lazy('login')



