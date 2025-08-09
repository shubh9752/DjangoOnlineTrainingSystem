from django.urls import path
from testapp import views

urlpatterns = [
    path('about', views.about),  # About page
    path('home', views.home),  # Home page
    path('contact', views.contact),  # Contact page
]
