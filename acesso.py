ac =  input("defina seu nivel de acesso(user,adm ou guest): ").upper()
count = 1
while ac != "USER" and ac != "ADM" and ac != "GUEST"  and ac != "":
    ac = input ("termo invalido, defina novamente: ").upper()
    if count == 3:
        print("acesso negado")
        exit()
    else:
        count += 1
if ac == "GUEST" :
    print("Bem vindo convidado!")
    exit()

if ac == "":
    print("bem vindo desconhecido")
    exit()

count = 1
from getpass import getpass
sen = getpass("digite sua senha: ").upper()
passwd = "12345"
while sen != passwd:
    en = getpass("senha invalida , digite novamente: ").upper()
    if count == 3:
        print("acesso negado")
        exit()
    else:
        count += 1
ge = input("qual seu genero(homem/mulher): ").upper()
    
while ge != "HOMEM" and ge != "MULHER":
    ge = input ("termo invalido, defina novamente: ").upper()

if ac == "USER" and ge == "HOMEM":
    print("Bem vindo usuario!")
    exit()
elif ac == "USER" and ge == "MULHER":
    print("Bem vindo usuaria!")
    exit()

if ac == "ADM" and ge == "HOMEM":
    print("Bem vindo administrador!")
elif ac == "ADM" and ge == "MULHER":
    print("Bem vindo administradora!")
else:
    exit()
