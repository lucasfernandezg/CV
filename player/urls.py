from django.urls import re_path
from player import views

urlpatterns = [
    re_path(r"^$", views.Index),
]
