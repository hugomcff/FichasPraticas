
##Introdução de dados
num=int(input("Introduza o numero: "))

##Condição
if num == 2:
    print("O numero {} é primo.".format(num))
else:
    while num > 1:
        for i in range(2,num):
            if num % i == 0:
                print("O numero {} não é primo.".format(num))
                break
            else:
                print("O numero {} é primo.".format(num))
                break
        break

##Não é possivel        
if num <= 1:
    print("Não existem numeros primos inferiores a 1, por isso o numero {} está excluido.",format(num))