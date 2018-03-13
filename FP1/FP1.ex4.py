nota1 = float(input("Escreva a 1º Nota: "))
nota2 = float(input("Escreva a 2º Nota: "))
nota3 = float(input("Escreva a 3º Nota: "))

media =float((nota1 * 25 + nota2 * 35 + nota3 * 40) /100)
media_int = int((nota1 * 25 + nota2 * 35 + nota3 * 40) //100)
media_modulo = int((nota1 * 25 + nota2 * 35 + nota3 * 40)%100)

#print("A média das notas é: {}\n A média inteira é: {}\n O resto da média é {}".format(media,media_int,media_modulo))

print("Média: ", media)
print("Média inteira: ", media_int)
print("Média modúlo ", media_modulo)