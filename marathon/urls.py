from django.urls import path

from . import views

app_name = "marathon"

urlpatterns = [
    path("", views.marathon_list, name="marathon"),
]