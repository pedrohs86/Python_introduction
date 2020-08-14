lista1 = [1, 2, 3, 4, 5]
lista2 = ["a", "b", "c", "d", "e"]
lista3 = ["f", "g", "x", "z"]

for numero, nome, valor in zip(lista1, lista2, lista3):
    print(numero, nome, valor)