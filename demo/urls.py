from django.urls import path
from .views import home, login,logout_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('home/', home, name='home'),
    path('', login, name='login'),
    path('logout/', logout_view, name='logout'),
]
