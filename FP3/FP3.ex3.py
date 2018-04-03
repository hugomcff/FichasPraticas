

#Imprimir texto
print("Voto candidato: 1/2/3/4.")
print("Voto nulo: 0.")
print("Voto em branco: 9.")
print("Introduza -1 para perminar")

##Introdução dos votos
voto=int(input("Insira o seu voto : "))

##Declaração de variaveis
candidato1 = 0
candidato2 = 0
candidato3 = 0
candidato4 = 0
votobranco = 0
votonulo = 0

##Ciclo contar
while voto != -1:
    if voto == 1:
        candidato1 += 1
    if voto == 2:
        candidato2 += 1
    if voto == 3:
        candidato3 += 1
    if voto == 4:
        candidato4 += 1
    if voto == 0:
        votobranco += 1
    if voto == 9:
        votonulo += 1

    ##Imprimir texto
    print("Voto candidato: 1/2/3/4.")
    print("Voto nulo: 0.")
    print("Voto em branco: 9.")
    print("Introduza -1 para perminar")

    ##Ler Votos
    voto=int(input("Insira o seu voto : "))

##Calculos
totalvotos= candidato1 + candidato2 + candidato3 + candidato4 + votonulo + votobranco
percentagem_candidato1 = (candidato1 * 100) / totalvotos
percentagem_candidato2 = (candidato2 * 100) / totalvotos
percentagem_candidato3 = (candidato3 * 100) / totalvotos
percentagem_candidato4 = (candidato4 * 100) / totalvotos
percentagem_branco = (votonulo * 100) / totalvotos
percentagem_nulo = ( votobranco * 100) / totalvotos

##Resultados
print()
print("Total de Votos: {}".format(totalvotos))
print()
print("Total Votos candidato 1: {}".format(candidato1))
print("Total Votos candidato 2: {}".format(candidato2))
print("Total Votos candidato 3: {}".format(candidato3))
print("Total Votos candidato 4: {}".format(candidato4))
print()
print("Total votos em branco: {}".format(votobranco))
print("Total votos nulos: {}".format(votonulo))
print()
print("Percentagem de votos candidato 1: {} %".format(percentagem_candidato1))
print("Percentagem de votos candidato 2: {} %".format(percentagem_candidato2))
print("Percentagem de votos candidato 3: {} %".format(percentagem_candidato3))
print("Percentagem de votos candidato 4: {} %".format(percentagem_candidato4))
print()
print("Percentagem votos em branco: {} %".format(percentagem_branco))
print("Percentagem votos nulos: {} %".format(percentagem_nulo))