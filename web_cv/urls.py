from django.urls import re_path
from web_cv import views

urlpatterns = [
    re_path(r"^$", views.Main_cv.as_view()),

]
