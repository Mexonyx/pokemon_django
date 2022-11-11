from django.shortcuts import render
from django.http import HttpResponse
from .models import Pokemon
import requests
# Create your views here.

def pokedex(request):
    url = "https://pokeapi.co/api/v2/pokemon/?limit=151"
    r = requests.get(url)
    print(r)
    jsonRequest = r.json()
    listpokemon = []
    
    for aPokemon in jsonRequest['results']:
        urlDetailPokemon = aPokemon['url']
        result = requests.get(urlDetailPokemon)
        detailPokemonJson = result.json()

        
        typesPokemon = ""
        # if properties == "types":
        #     for type in properties['types']:
        #         typesPokemon += type['type']['name']
        # if properties == "id":
        #     idPokemon = properties['id']
        # if properties == "sprites":
        #     imageDetailPokemon = properties['sprites']['other']['official-artwork']['front_default']
        # if properties == "types":
        #     typeDetailPokemon = properties['types']
        listpokemon.append(Pokemon(id=detailPokemonJson['id'], name = detailPokemonJson['name'],urlImage = detailPokemonJson['sprites']['other']['official-artwork']['front_default'], type = detailPokemonJson['types'][0]['type']['name']))

    context = {"pokemonList" : listpokemon} 

    return render(request,'pokedex/index.html', context)