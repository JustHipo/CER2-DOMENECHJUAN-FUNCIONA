
from django.urls import path
from django.http.response import HttpResponse
from . import views
from django.contrib import admin
from webapp.views import home, register_view


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home),
    path("register/", views.register_view ,name="register"),
    path("home/", views.home, name="home"),
    
]
