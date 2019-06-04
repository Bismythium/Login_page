from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #/main_page/login/
    path('login/', views.pagelogin, name='login'),
     path('loginnew/', views.pageloginnew, name='loginnew'),
    #/main_page/signup/
    path('signupnew/', views.signupnew, name='signupnew'),
    path('signup/', views.signup, name='signup'),
]