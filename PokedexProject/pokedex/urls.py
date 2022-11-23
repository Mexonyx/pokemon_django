from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.pokedex, name="pokedex"),
    path('pokedex/detailed/<int:idPokemon>', views.detailedPokemon, name="detailedPokemon"),

    path('page/<int:pageNumber>', views.pokedex, name="previousPage"),
    path('page/<int:pageNumber>', views.pokedex, name="nextPage")
]
