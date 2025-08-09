from django.urls import path
from OTS.views import *


urlpatterns = [
    path('', home),
    path('candidateRegistrationForm/', candidateRegistrationForm),
    path('candidateRegistration/', candidateRegistration),
    path('loginViews', loginViews),
    path('candidateHome/', candidateHome),
    path('testpaper/', testpaper),
    path('calculateTestResults/', calculateTestResults),
    path('testResultHistory/', testResultHistory),
    path('showTestResult/', showTestResult),
    path('logoutView/', logoutView),


]
