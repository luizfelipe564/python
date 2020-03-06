ac =  input("defina seu nivel de acesso(user,adm ou guest): ").upper()
if ac != "USER" and ac != "ADM" and ac != "GUEST"  and ac != "":
    ac = input ("termo invalido, defina novamente: ").upper()

if ac == "":
    print("bem vindo desconhecido")
    exit()

ge = input("qual seu genero(homem/mulher): ").upper()
if ge != "HOMEM" and ge != "MULHER":
    ge = input ("termo invalido, defina novamente: ").upper()

if ac == "USER" and ge == "HOMEM":
    print("Bem vindo usuario!")
elif ac == "USER" and ge == "MULHER":
    print("Bem vindo usuaria!")
    

if ac == "ADM" and ge == "HOMEM":
    print("Bem vindo administrador!")
elif ac == "ADM" and ge == "MULHER":
    print("Bem vindo administradora!")
    

if ac == "GUEST" and ge == "HOMEM":
    print("Bem vindo convidado!")
elif ac == "GUEST" and ge == "MULHER":
    print("Bem vindo convidada!")
    
    
else:
    exit()
