from django.shortcuts import render
from django.http import HttpResponse, request
from .models import Pokemon
import requests
from django.core.paginator import Paginator
# Create your views here.

def getListPokemons():
    url = "https://pokeapi.co/api/v2/pokemon/?limit=4"
    r = requests.get(url)
    jsonRequest = r.json()
    listpokemon = []

    for aPokemon in jsonRequest['results']:
        urlDetailPokemon = aPokemon['url']
        result = requests.get(urlDetailPokemon)
        detailPokemonJson = result.json()
        listpokemon.append(Pokemon(id=detailPokemonJson['id'], name=detailPokemonJson['name'],
                                   urlImage=detailPokemonJson['sprites']['other']['official-artwork']['front_default'],
                                   type=detailPokemonJson['types'][0]['type']['name'], 
                                   weight=detailPokemonJson['weight'])),

    return listpokemon

def getOnePokemon(idPokemon):
    url = "https://pokeapi.co/api/v2/pokemon/" + str(idPokemon)
    r = requests.get(url)
    jsonRequest = r.json()
    thePokemon = Pokemon(id=idPokemon, name=jsonRequest['species']['name'],
                         urlImage=jsonRequest['sprites']['other']['official-artwork']['front_default'],
                         type=jsonRequest['types'][0]['type']['name'])

    return thePokemon

def pokedex(request):
    pokemonList = getListPokemons()
    context = {"pokemonList" : pokemonList}
    return render(request,'pokedex/index.html', context)

def detailedPokemon(request, idPokemon):
    thePokemon = getOnePokemon(idPokemon)
    context = {"pokemon": thePokemon}
    return render(request, "pokedex/detailedPokemon.html" , context)

def searchBar(request):
    allPokemon = getListPokemons()
    filteredPokemonList = []
    for pokemon in allPokemon:
        if request.GET.get('search') in pokemon.name:
            filteredPokemonList.append(pokemon)
    context = {"pokemonList" : filteredPokemonList}
    return render(request, "pokedex/index.html", context)


def pokemonTeams(request):

    return render(request, 'pokedex/myTeams.html')

def createTeam(request):
    listPokemon = getListPokemons()


    context = {"pokemonList" : listPokemon}

    return render(request, 'pokedex/createTeam.html', context)