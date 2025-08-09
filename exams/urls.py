from django.urls import path
from exams import views

urlpatterns = [
    path('testpaper',views.testpaper),
    path('results', views.results),
]
