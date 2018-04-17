
##Função
def figura(linhas, colunas, caracter) :
     
    for i in range(1, linhas + 1) :
        for j in range(1, colunas + 1) :
            if (i == 1 or i == linhas or j == 1 or j == colunas) :
                print(caracter, end="")            
            else :
                print(" ", end="")            
        print()
 

##Programa
linhas = int(input('Introduza o numero de linhas: '))
colunas = int(input('Introduza o numero de colunas: '))
caracter = input('Escolha o caracter da figura: ')
figura(linhas, colunas, caracter)