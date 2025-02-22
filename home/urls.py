from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("home/", views.home, name="home"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("login/", views.login, name="login"),
    path("auth/", views.auth, name="auth"),
    
    path("shelter/", views.shelter, name="shelter"),
    path("shelter/add/", views.shelter_add, name="shelter-add"),
    path("save-shelter/", views.save_shelter, name="save-shelter"),
    path("delete-shelter/<int:id>/", views.delete_shelter, name="delete-shelter"),
    path("edit-shelter/<int:id>/", views.edit_shelter, name="edit-shelter"),
    path("update-shelter/<int:id>/", views.update_shelter, name="update-shelter"),

    # Kriteria
    path("kriteria/", views.kriteria, name="kriteria"),
    path("kriteria/add/", views.kriteria_add, name="kriteria-add"),
    path("save-kriteria/", views.save_kriteria, name="save-kriteria"),
    path("delete-kriteria/<int:id>/", views.delete_kriteria, name="delete-kriteria"),
    path("edit-kriteria/<int:id>/", views.edit_kriteria, name="edit-kriteria"),
    path("update-kriteria/<int:id>/", views.update_kriteria, name="update-kriteria"),
    
    path('analyze/', views.analyze_data, name='analyze_data'),
    
    # Decision Tree
    path("decision-tree/", views.decision_tree, name="decision-tree"),
    
    # Laporan
    path("laporan/", views.laporan, name="laporan"),
    
    # Classifications save
    path("save-classification/", views.save_classification, name="save-classification"),
]


