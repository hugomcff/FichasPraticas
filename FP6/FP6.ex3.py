##Exercicio 3


##Comnteudo da Lista
def conteudo(myList):
    for i in range(len(myList)):
        print(myList[i],end=" ")

##Calcular o dobro
def dobro(myList):
    for i in range(len(myList)):
        print(myList[i]*2,end=" ")

##Soma do conteudo
def soma(myList):
    sum = 0
    for numeros in myList:
        sum += numeros
    return sum 

##Media
def media(myList):
    sum = 0
    for numeros in myList:
        sum += numeros
    return sum /len(myList)

numeros = []

x = 1

while x <= 10:
    n = int(input("Introduza um número: [ %s ]: "%x))
    numeros.append(n)
    x += 1

print()
print("\nConteúdo da lista:") 
conteudo(numeros)
print("\nDobro de cada elemento:") 
dobro(numeros)
print("\n\nSoma da lista:", soma(numeros))
print("\nMedia da lista:", media(numeros))
print("\nMaior número da lista é:", max(numeros))
print("\nMenor número da lista é:", min(numeros))