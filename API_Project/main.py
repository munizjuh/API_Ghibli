import requests
import csv

print("Bem vinde a biblioteca de animações do estúdio Ghibli!")
print("Vamos Salvar algumas informações sobre os filmes, personagens, etc para você :D")

respfilme = requests.get("https://ghibliapi.herokuapp.com/films")
filmes = respfilme.json()
filmes_ghibli = open('filmes_ghibli.csv', 'w', encoding= "utf-8")
csv_writer = csv.writer(filmes_ghibli)
count = 0
print("Salvando as principais informações sobre as produções dos filmes...")

for filme in filmes:
    if count == 0:
        header = filme.keys()
        csv_writer.writerow(header)
        count += 1

    csv_writer.writerow(filme.values())

filmes_ghibli.close()

respPersonagens = requests.get("https://ghibliapi.herokuapp.com/people")
personagens = respPersonagens.json()
personagens_ghibli = open('personagens_ghibli.csv', 'w', encoding= "utf-8")
csv_writer = csv.writer(personagens_ghibli)
count = 0
print("Salvando todas as características dos personagens dos filmes...")

for personagem in personagens:
    if count == 0:
        header = personagem.keys()
        csv_writer.writerow(header)
        count += 1

    csv_writer.writerow(personagem.values())

personagens_ghibli.close()

respLocalizacoes = requests.get("https://ghibliapi.herokuapp.com/locations")
localizacoes = respLocalizacoes.json()
localizacoes_ghibli = open('localizacoes_ghibli.csv', 'w', encoding= "utf-8")
csv_writer = csv.writer(localizacoes_ghibli)
count = 0
print("Salvando informaçõe sobres as localizações onde se passam os filmes filmes...")

for localizacao in localizacoes:
    if count == 0:
        header = personagem.keys()
        csv_writer.writerow(header)
        count += 1

    csv_writer.writerow(personagem.values())

localizacoes_ghibli.close()

respespecies = requests.get("https://ghibliapi.herokuapp.com/species")
especies = respespecies.json()
especies_ghibli = open('especies_ghibli.csv', 'w', encoding= "utf-8")
csv_writer = csv.writer(especies_ghibli)
count = 0
print("Salvando as informações principais sobre as criaturas dos filmes...")

for especie in especies:
    if count == 0:
        header = especie.keys()
        csv_writer.writerow(header)
        count += 1

    csv_writer.writerow(especie.values())

especies_ghibli.close()

respveiculos = requests.get("https://ghibliapi.herokuapp.com/vehicles")
veiculos = respveiculos.json()
veiculos_ghibli = open('veiculos_ghibli.csv', 'w', encoding= "utf-8")
csv_writer = csv.writer(veiculos_ghibli)
count = 0
print("Salvando as informações principais sobre os veículos que aparecem nos filmes...")

for veiculo in veiculos:
    if count == 0:
        header = veiculo.keys()
        csv_writer.writerow(header)
        count += 1

    csv_writer.writerow(veiculo.values())

veiculos_ghibli.close()

print("Todas as informações foram salvas :D")
