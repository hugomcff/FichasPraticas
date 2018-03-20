
##Introdulão das notas
nota1 = float(input("Escreva a 1º Nota: "))
nota2 = float(input("Escreva a 2º Nota: "))
nota3 = float(input("Escreva a 3º Nota: "))

##Verificar se as notas sao superiores a 0 e inferiores a 20
if nota1 >= 0 and nota1 <= 20:
    if nota2 >= 0 and nota2 <= 20:
        if nota3 >= 0 and nota3 <= 20:
            media =float((nota1 * 25 + nota2 * 35 + nota3 * 40) /100)
            if media > 9.5:
                print("O aluno encontra-se aprovado com media de: ",media)
            else:
                print("O aluno encontra-se reprovado com media de: ",media)
        else:
            print("A nota tem que ser superior a 0 e inferior a 20.")
    else:
        print("A nota tem que ser superior a 0 e inferior a 20.")
else:
    print("A nota tem que ser superior a 0 e inferior a 20.")


