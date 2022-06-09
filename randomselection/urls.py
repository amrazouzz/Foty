from django.urls import path
from . import views

urlpatterns = [
    path("",views.home, name = "home"),
    path('random-selection/',views.selection,name = "random-selection"),
    path('create_new_selection/',views.createNewSelection, name="create_new_selection"),
    path('add_new_player/',views.AddPlayer,name="add_new_player"),
    path('update_player/<str:pk>/',views.UpdatePlayer,name="update_player"),
    path('players_list/',views.PlayersList,name="players_list"),
    path('delete_player/<str:pk>/',views.deletePlayer,name="delete_player"),
]
