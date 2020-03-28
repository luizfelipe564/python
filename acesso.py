ac =  input("defina seu nivel de acesso(user,adm ou guest): ").upper()

while ac != "USER" and ac != "ADM" and ac != "GUEST"  and ac != "":
    ac = input ("termo invalido, defina novamente: ").upper()

if ac == "GUEST" :
    print("Bem vindo convidado!")
    exit()
    
if ac == "":
    print("bem vindo desconhecido")
    exit()

sen = input("digite sua senha: ")    
while sen != "12345":
    sen = input ("senha invalida , digite novamente: ").upper()

ge = input("qual seu genero(homem/mulher): ").upper()
while ge != "HOMEM" and ge != "MULHER":
    ge = input ("termo invalido, defina novamente: ").upper()

if ac == "USER" and ge == "HOMEM":
    print("Bem vindo usuario!")
elif ac == "USER" and ge == "MULHER":
    print("Bem vindo usuaria!")
    

if ac == "ADM" and ge == "HOMEM":
    print("Bem vindo administrador!")
elif ac == "ADM" and ge == "MULHER":
    print("Bem vindo administradora!")
    
    
else:
    exit()
