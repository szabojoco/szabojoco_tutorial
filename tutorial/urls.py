from django.urls import path
from . import views
from tutorial.forms import AuthenticationNewForm, PasswordChangeNewForm
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("login/", auth_views.LoginView.as_view(form_class=AuthenticationNewForm), name="login"),
    path('password_change/', auth_views.PasswordChangeView.as_view(form_class=PasswordChangeNewForm),
         name="password_change"),
    path('sign_up/', views.sign_up, name='sign_up'),
    path("", views.HomeTemplateView.as_view(), name="home_page"),
    path('tutorial/', views.tutorial_view, name='tutorial_view'),
    path('tutorial_content/<int:tutorial_id>/', views.tutorial_content, name='tutorial_content'),
    path('tutorial_detail/<int:tutorial_id>/', views.tutorial_detail, name='tutorial_detail'),
    path('tutorial_buy/<int:tutorial_id>/', views.tutorial_buy, name='tutorial_buy'),
    path('tutorial/process_payment/<int:tutorial_id>/', views.process_payment, name='process_payment'),
]
