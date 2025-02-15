from django.urls import path, re_path
from django.shortcuts import redirect
from .views import *

urlpatterns = [
    path("", home_view, name="home_view"),
    re_path(r'^.*$', lambda request: redirect('/')),
]
