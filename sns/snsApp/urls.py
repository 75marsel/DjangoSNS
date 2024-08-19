from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_view, name="home"),
    path("profile_list/", views.profile_list_view, name="profile_list"),
]
