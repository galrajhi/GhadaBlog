from django.urls import path
from django.urls.resolvers import URLPattern
from . import views
from .views import HomeView, AddPostView, ArticaleDetailView, UpdatePostView, DeletePost




urlpatterns  = [
    
    path('', HomeView.as_view(), name = 'index'),
    path('about', views.about, name= 'About'),
    path('contact', views.contact, name = 'contact'),
    path('Article/<str:pk>', ArticaleDetailView.as_view(),name= 'Article'),
    path('addpost/', AddPostView.as_view(), name='addpost'),
    path('Article/edit/<str:pk>', UpdatePostView.as_view(), name='update_post'),
    path('Article/<str:pk>/Delete', DeletePost.as_view(), name='delete_post')
    


]