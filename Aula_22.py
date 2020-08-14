arquivo = open("Arquivo teste.txt")
texto = arquivo.read()
print(texto)
arquivo.close()

w = open("Arquivo2.txt", "w")
w.write("This my new file")
w.close()

a = open("Arquivo teste.txt", "a")
a.write("This my new file\n")
a.close()