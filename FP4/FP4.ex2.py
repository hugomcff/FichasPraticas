

##Variaveis
EURO = 0.81319
USD = 1.22958

##Função
def conversor(num,simb) :
    if simb == "E":
        res = num * EURO
    elif simb == "D":
        res = num * USD
    return res



##Programa
print("Para Euro use: E")
print("Para Dollar use: D")
print()

numero= int(input("Introduza o valor: "))
simbolo = (input("Introduza a moeda: "))

res = conversor(numero,simbolo)
print(round(res, 4))
