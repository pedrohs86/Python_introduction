import math as m

def questao1():
    idade = int(input("Digite a sua idade: "))
    if idade >= 18:
        print("Você é maior de idade")
    else:
        print("Você é menor de idade")
# questao1()

def questao2():
    for i in [0, 1]:
        nota = int(input("Digite uma nota: "))
        if nota >= 6:
            print("Aprovado")
        else:
            print("Reprovado")
# questao2()

def questao3():
    a = int(input("Digite o parametro 'a' da equação: "))
    b = int(input("Digite o parametro 'b' da equação: "))
    c = int(input("Digite o parametro 'c' da equação: "))
    delta = b**2 - 4*a*c 
    if delta >0:
        x1 = (-b + m.sqrt(delta))/2*a
        x2 = (-b - m.sqrt(delta))/2*a
        print(x1)
        print(x2)
    else:
        print("Essa equação tem raizes complexas")
# questao3()

def questao4(lista: list):
    return sorted(lista)

# print(questao4([21,2,12,3243312,32132,3131,1,1,3]))

def questao5():
    a = int(input("Digite um numero: "))
    b = int(input("Digite outro numero: "))
    c = input("Digite a operação que deseja realizar: ")
    if c == "+":
        print(a + b)
    elif c == "-":
        print(a - b)
    elif c == "*":
        print(a*b)
    elif c == "/":
        print(a/b)
    else:
        print("operador invalido")
questao5()