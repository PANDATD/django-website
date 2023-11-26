from django.urls import path 
from . import views 

# following imports are required.

urlpatterns = [
    path('',views.home, name='blog-home'),
    # Following path for home page 
    path('about/', views.about, name='blog-about'),
    # Following path for about page
    ]

