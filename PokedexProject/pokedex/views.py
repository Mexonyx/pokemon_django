from django.shortcuts import render
from django.http import HttpResponse
import requests
# Create your views here.

def pokedex(request):
    url = "https://pokeapi.co/api/v2/pokemon/?limit=151"
    r = requests.get(url)
    print(r)
    jsonRequest = r.json()
    listpokemon = []
    for pokemon in jsonRequest['results']:
        listpokemon.append(pokemon['name'] + ' ')

    return HttpResponse(listpokemon)