from django.urls import path

from . import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.LOginuser.as_view(), name='login'),
    path('logout/', views.logouserout, name='logout')

] 



