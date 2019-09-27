#-*- coding: utf-8 -*-
# coment test
mensagem = "eae mano"
# print ("Hello world!")
# print ('Olá mundo!')

""" 
    comentario teste
"""
# print ( 2**2 ) #potência
# print ( 10%3 ) #Resto da divisão
# print (mensagem)

var1 = 1
var2 = 1.1
var3 = 'string'
var4 = True

x = 2
y = 10
s = x

# print (x == y)
# print (x < y)
# print (x>y)
# print (soma>y)
print (s > y and x == y)
print (s > y or x == y)

x = 3

# print (x==y)
# print (x < y)
# print (x>y)
print (s > y and x == y)
print (s > y or x == y)

if s>y:
    print ('maior')
else:
    print("menor")
    
a = -2
b = -1
    
if b > a:
    if b > 0:
        print ("b é maior que a\nb é positivo")
    else:
        print ("b é maior que a\nb é negativo")
else:
    print ("b é menor que a")

x = 1
y =2

if x == y:
    print("numeros iguais")
elif x > y:
    print("x maior que y")
elif y > x:
    print("y maior que x")
else:
    print("Bugou")