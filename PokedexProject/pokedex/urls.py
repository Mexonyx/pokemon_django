from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.pokedex, name="pokedex"),
    path('pokedex/detailed/<int:idPokemon>', views.detailedPokemon, name ="detailedPokemon"),
    path('searchBar', views.searchBar, name="searchPokemon")
]