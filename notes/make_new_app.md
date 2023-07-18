1.Create app
    python manage.py startapp app_name

2.In app_name/view.py
from django.shortcuts import render
from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("Hello, World! This is your new app.")

3.In project/settings.py, in INSTALLED_APPS:
INSTALLED_APPS = [
    'app_name',
]

4.In project/urls.py:
from django.urls import path
from app_name.views import hello_world

urlpatterns = [
    path('hello/', hello_world, name='hello_world'),
]
