from django.contrib import admin
from django.urls import path, include
from tutorial import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include('tutorial.urls')),
    path('', include('django.contrib.auth.urls')),
    path('my-tutorials/', views.my_tutorials, name='my_tutorials'),
    path('tutorial/buy/<int:tutorial_id>/', views.tutorial_buy, name='tutorial_buy'),
    path('tutorial/purchased/<int:tutorial_id>/', views.purchased_tutorial, name='purchased_tutorial'),
]
