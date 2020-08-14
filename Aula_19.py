a = "Pedro"
b = "Amanda"

concatenar =" " + a + " " + b + " "

tamanho = len(concatenar)
print(tamanho)
print(a[1:4])

print(concatenar.lower())
print(concatenar.upper())
print(concatenar.strip())

minha_string = "O rato roeu a roupa do rei de Roma"
minha_lista = minha_string.split("r")
print(minha_lista)

busca = minha_string.find("rei")
print(busca)

replace = minha_string.replace("rei", "rainha")
print(replace)