from django.urls import path
# from .views import shelter_list
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("login/", views.login, name="login"),
    path("auth/", views.auth, name="auth"),
    path("shelter/", views.shelter, name="shelter"),
    path("shelter/add/", views.shelter_add, name="shelter-add"),
    path("save-shelter/", views.save_shelter, name="save-shelter"),
    path("delete-shelter/<int:id>/", views.delete_shelter, name="delete-shelter"),
    path("edit-shelter/<int:id>/", views.edit_shelter, name="edit-shelter"),
    path("update-shelter/<int:id>/", views.update_shelter, name="update-shelter"),

    
]


