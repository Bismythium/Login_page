from django.urls import path

from . import views

app_name= 'siteusers'
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.pagelogin, name='login'),
]
