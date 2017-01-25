import sys
from bs4 import BeautifulSoup
import argparse
import requests

r = requests.get('http://pokemondb.net/pokedex/national#gen-1')
soup = BeautifulSoup(r.text)

names = []
for pokemon_list in soup.findAll('span', { 'class': 'infocard-tall'}):
    for link in pokemon_list.findAll('a', { 'class': 'ent-name'}):
        names.append(link.text)

for name in names:
    parsedName = name.lower() # Make names lowercase
    parsedName = parsedName.replace("'", "") # Remove apostraphes
    parsedName = parsedName.replace(".", "-") # Remove periods
    # TODO - Handle Nidoran
    print("Downloading {}".format(name))
    url = "https://img.pokemondb.net/sprites/x-y/normal/{}.png".format(parsedName)
    pkmn_r = requests.get(url)
    if pkmn_r.status_code != 200:
        print("Error downloading {}".format(name))
        continue
    
    f = open("./sprites/{}.png".format(name.lower()), 'wb')
    f.write(pkmn_r.content)
    f.close()