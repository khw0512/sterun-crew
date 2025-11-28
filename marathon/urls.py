from django.urls import path

from . import views

app_name = "marathon"

urlpatterns = [
    path("", views.marathon_list, name="marathon_list"),
    path('parti-me/<str:key>', views.parti_me, name='parti_me'),
    path('del_parti/<str:key>', views.del_parti, name='del_parti'),
]