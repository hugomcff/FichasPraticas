##Exercicio 2

##Contar e Posicao
def  quantidade(carater):  
    simbolo = input("Introduza 1 caratere: ")
    contar = carater.count(simbolo)
    print("A letra {} existe: {} vezes.".format(simbolo, contar)) 
    for i,j in enumerate(carater):
        if j == simbolo:
            print("A letra {} encontra-se na posição {}.".format(j,i))

carater = []
x = 1
while x <= 10:
    c = input("Introduza um carater: ")
    carater.append(c)
    x += 1

##Chamar quantidade
quantidade(carater)