from django.urls import path
from django.contrib.auth.views import LoginView
app_name = 'users'
from . import views

urlpatterns = [
    path('', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout', views.logout_views, name = 'logout'),
]
