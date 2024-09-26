from django.urls import path
from . import views
from .views import send_email, email_success, email_error

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('send_email/', views.send_email, name='send_email'),
    #path('email_template/', views.email_template, name='email_template'),
    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('email_success/', email_success, name='success_url'),
    path('email_error/', email_error, name='error_url'),
    path('logout/', views.logout_view, name='logout'),
    path('settings/', views.settings, name='settings'),  # Add this line








]
