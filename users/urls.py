from . import views
from django.urls import path
from django.contrib.auth import views as auth_views

from .views import *

app_name = "users"
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name = "users/login.html"), name = "login"),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup, name='signup'),
]