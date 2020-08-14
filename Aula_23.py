# -*- coding: utf-8 -*-
lista = ["abacaxi", "melancia", "abacate"]
lista.append("limão")
# print(lista)
lista2 = [1, 2, 3, 4, 5]

if 3 in lista2:
    print("Achado")
    
del lista[2:]
# print(lista)

lista3 = [2,3,4,21,2,21,4,4435,354,435,543,543,76,54,34]
lista3.reverse()
# lista3.sort(reverse=True)
# lista3 = sorted(lista3)

print(lista3)

dicionario_sites = {"Diego": "diegomariano.com", "Google": "google.com", "Udemy": "udemy.com"}
 
for chave in dicionario_sites:
    print(dicionario_sites[chave])

for chave in dicionario_sites.keys():
    print(chave)