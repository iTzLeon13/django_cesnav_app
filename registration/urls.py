from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('participants/', views.view_participants, name='view_participants'),
    path('create_teams/', views.create_teams, name='create_teams'),
]