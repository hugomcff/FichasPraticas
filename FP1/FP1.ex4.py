nota1 = float(input("Introduza a 1º nota: "))
nota2 = float(input("Introduza a 2º nota: "))
nota3 = float(input("Introduza a 3º nota: "))

nota1p = nota1 * 1.25
nota2p = nota2 * 1.35
nota3p = nota3 * 1.45

media = (nota1p + nota2p + nota3p) / 3

print("Média Ponderada: ", media)