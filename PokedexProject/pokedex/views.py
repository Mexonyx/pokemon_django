from django.shortcuts import render
from django.http import HttpResponse, request
from .models import Pokemon
from django.urls import reverse
import requests
from django.core.paginator import Paginator


# Create your views here.

def getListPokemons(pageNumber):

    pagination = pageNumber*20
    url = "https://pokeapi.co/api/v2/pokemon/?offset=" + str(pagination) + "&limit=20"
    r = requests.get(url)
    jsonRequest = r.json()

    listPokemon = []

    for aPokemon in jsonRequest['results']:
        urlDetailPokemon = aPokemon['url']
        result = requests.get(urlDetailPokemon)
        detailPokemonJson = result.json()
        listPokemon.append(Pokemon(id=detailPokemonJson['id'], name=detailPokemonJson['name'],
                                   urlImage=detailPokemonJson['sprites']['other']['official-artwork']['front_default'],
                                   type=detailPokemonJson['types'][0]['type']['name']))

    return listPokemon


def getOnePokemon(idPokemon):
    url = "https://pokeapi.co/api/v2/pokemon/" + str(idPokemon)
    r = requests.get(url)
    jsonRequest = r.json()
    thePokemon = Pokemon(id=idPokemon, name=jsonRequest['species']['name'],
                         urlImage=jsonRequest['sprites']['other']['official-artwork']['front_default'],
                         type=jsonRequest['types'][0]['type']['name'])

    return thePokemon


def pokedex(request, pageNumber=0):
    pokemonList = getListPokemons(pageNumber)
    context = {"pokemonList": pokemonList, "pageNumber": pageNumber}
    return render(request, 'pokedex/index.html', context)


def detailedPokemon(request, idPokemon):
    thePokemon = getOnePokemon(idPokemon)
    context = {"pokemon": thePokemon}
    return render(request, "pokedex/detailedPokemon.html", context)


def pokemonTeams(request):
    return render(request, 'pokedex/myTeams.html')


def createTeam(request):
    listPokemon = getListPokemons()

    context = {"pokemonList": listPokemon}

    return render(request, 'pokedex/createTeam.html', context)
