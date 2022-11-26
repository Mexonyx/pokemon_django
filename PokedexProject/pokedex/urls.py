from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.pokedex, name="pokedex"),

    path('detailed/<int:idPokemon>', views.detailedPokemon, name ="detailedPokemon"),
    path('searchBar', views.searchBar, name="searchPokemon"),
    path('page/<int:pageNumber>', views.pokedex, name="previousPage"),
    path('page/<int:pageNumber>', views.pokedex, name="nextPage"),
    path('teams/', views.pokemonTeams, name="teams"),
]


