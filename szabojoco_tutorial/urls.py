from django.contrib import admin
from django.urls import path, include

from tutorial import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("tutorial/", views.tutorial_view, name="tutorial_view"),
    path("", include("home.urls")),
]
