
##Função
def fact(n):
    if n == -1:
        return 0
    elif fact(n - 1):
        return n
    print(n)

##Programa
num = int(input('Introduza um numero: '))
fact(num)

