from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.pokedex, name="pokedex"),
    path('pokemonsTeams', views.pokemonTeams, name="pokemonsTeams"),
    path('createTeam', views.createTeam, name="createTeam")
]