
#Introdução de dados
saldo = float(input("Introduza o saldo da sua conta: "))
#Erro saldo
if saldo < 0:
    saldo = float(input("Introduza o saldo da sua conta: "))
print ("Qual a operação que pretende: ")
print ("1-Creditar: ")
print ("2-Debitar: ")
#Seleção da operação
operacao = input("Introduza a operação (1/2):")
#Creditar
if operacao == "1":
    creditar = float(input("Introduza o valor a creditar: "))
    res = saldo + creditar
    print ("Crédito realizado com sucesso!")
    print ("Saldo: ", res)
#Debitar
if operacao == "2":
    debitar = float(input("Introduza o valor a debitar: "))
    res = saldo - debitar
    if res < 0:
        print ("Operação impossivel por saldo insuficiente: ")
    else:
        print ("Débito realizado com sucesso!")
        print ("Saldo: ", res)
