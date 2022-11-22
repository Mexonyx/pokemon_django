from django.shortcuts import render
from django.http import HttpResponse
from .models import Pokemon
import requests
# Create your views here.

def getListPokemons():
    url = "https://pokeapi.co/api/v2/pokemon/?limit=151"
    r = requests.get(url)
    jsonRequest = r.json()
    listpokemon = []

    for aPokemon in jsonRequest['results']:
        urlDetailPokemon = aPokemon['url']
        result = requests.get(urlDetailPokemon)
        detailPokemonJson = result.json()
        listpokemon.append(Pokemon(id=detailPokemonJson['id'], name=detailPokemonJson['name'],
                                   urlImage=detailPokemonJson['sprites']['other']['official-artwork']['front_default'],
                                   type=detailPokemonJson['types'][0]['type']['name']))

    return listpokemon

def pokedex(request):
    pokemonList = getListPokemons()
    context = {"pokemonList" : pokemonList}
    return render(request,'pokedex/index.html', context)


def pokemonTeams(request):

    return render(request, 'pokedex/myTeams.html')

def createTeam(request):
    listPokemon = getListPokemons()


    context = {"pokemonList" : listPokemon}

    return render(request, 'pokedex/createTeam.html', context)