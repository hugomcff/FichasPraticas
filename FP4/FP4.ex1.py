
##Função validar
def login(utilizador,password) :
    user = "aluno"
    passw = "estg2018"

    if utilizador == user and password == passw:
        return True
    return False

def validar() :
    contar = 0
    while contar != 3:
        utilizador=input("Utilizador : ")
        password=input("Password : ")
        if login(utilizador,password) :
            print("Inicio de sessão efetuado com sucesso!")
            break
        else:
            print("Erro de inicio de sessão!")
        contar += 1
    if contar >= 3:
        print("Limite maximo de tentativas atingido")  
        

##Programa
validar()
  