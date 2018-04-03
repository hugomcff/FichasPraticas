

##Ler numero
num=int(input("Introduza um numero inteiro: "))

##For numeros anteriores
print("Os 5 números anteriores a {} são: ".format(num))
for i in range(num-1, num-6, -1):
    print(i, end=" ")

##Deixar espaço
print()

##For numeros seguintes
print("Os 5 números seguintes a {} são: ".format(num))
for i in range(num+1, num+6, 1):
    print(i, end=" ")