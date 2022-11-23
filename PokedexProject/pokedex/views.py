from django.shortcuts import render
from django.http import HttpResponse, request
from .models import Pokemon
from django.urls import reverse
import requests
from django.core.paginator import Paginator


# Create your views here.

def getListPokemons(pageNumber=0):
    pagination = (pageNumber-1) * 20
    if pagination != -20:
        url = "https://pokeapi.co/api/v2/pokemon/?offset=" + str(pagination) + "&limit=20"
    else:
        url= "https://pokeapi.co/api/v2/pokemon/?limit=151"
    r = requests.get(url)
    jsonRequest = r.json()

    listPokemon = []

    for aPokemon in jsonRequest['results']:
        urlDetailPokemon = aPokemon['url']
        resulturlDetail = requests.get(urlDetailPokemon)
        detailPokemonJson = resulturlDetail.json()
        listPokemon.append(
            Pokemon(id=detailPokemonJson['id'], name=detailPokemonJson['name'],
                    urlImage=detailPokemonJson['sprites']['other']['official-artwork']['front_default'],
                    type=detailPokemonJson['types'][0]['type']['name'], 
                    )),
    return listPokemon


def getOnePokemon(idPokemon):
    url = "https://pokeapi.co/api/v2/pokemon/" + str(idPokemon)
    r = requests.get(url)
    jsonRequest = r.json()
    
    urlSpeciesPokemon = jsonRequest['species']['url']
    resulturlSpeciesPokemon = requests.get(urlSpeciesPokemon)        
    speciesPokemon = resulturlSpeciesPokemon.json()
        
    thePokemon = Pokemon(id=idPokemon, name=jsonRequest['species']['name'],
                         urlImage=jsonRequest['sprites']['other']['official-artwork']['front_default'],
                         type=jsonRequest['types'][0]['type']['name'], 
                         weight=jsonRequest['weight'],
                         description=speciesPokemon['flavor_text_entries'][0]['flavor_text'])

    return thePokemon


def pokedex(request, pageNumber=1):
    pokemonList = getListPokemons(pageNumber)

    prevPage = pageNumber-1
    prevPage2nd = pageNumber - 2
    prevPage3rd = pageNumber - 3

    nextPage = pageNumber + 1
    nextPage2nd = pageNumber + 2
    nextPage3rd = pageNumber + 3

    context = {"pokemonList": pokemonList,
               "pageNumber": pageNumber,
               "nextPage": nextPage,
               "nextPage2nd": nextPage2nd,
               "nextPage3rd": nextPage3rd,
               "prevPage": prevPage,
               "prevPage2nd": prevPage2nd,
               "prevPage3rd": prevPage3rd
               }

    return render(request, 'pokedex/index.html', context)


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
    context = {"pokemonList" : filteredPokemonList, "pageNumber": -1}
    return render(request, "pokedex/index.html", context)

def pokemonTeams(request):
    return render(request, 'pokedex/myTeams.html')


def createTeam(request):
    listPokemon = getListPokemons()

    context = {"pokemonList": listPokemon}

    return render(request, 'pokedex/createTeam.html', context)
