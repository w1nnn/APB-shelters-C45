from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("login/", views.login, name="login"),
    path("auth/", views.auth, name="auth"),
    path("shelter/", views.shelter, name="shelter"),
    
]


