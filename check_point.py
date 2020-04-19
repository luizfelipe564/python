
ac =  input("defina seu nivel de acesso(user,adm ou guest): ").upper()
count = 1
while ac != "USER" and ac != "ADM" and ac != "GUEST"  and ac != "":
    ac = input ("termo ( {} ) invalido, defina novamente: ".format(ac)).upper()
    if count == 3:
        print("acesso negado,{} não é um acesso valido".format(ac))
        exit()
    else:
        count += 1

if ac == "GUEST" :
    print("Bem vindo convidado!")
    exit()

if ac == "":
    print("acesso negado, desconhecido")
    exit()

from getpass import getpass
sen = getpass("digite sua senha: ").upper()
passwd = "12345"
while sen != passwd:
    sen = getpass("senha invalida , digite novamente: ").upper()
    if count == 3:
        print("acesso negado, muitas tentativas")
        exit()
    else:
        count += 1

ge = input("qual seu genero(homem/mulher): ").upper()
while ge != "HOMEM" and ge != "MULHER":
    ge = input ("termo ( {} ) desconhecido, defina novamente(homem/mulher): ".format(ge)).upper()
    if count == 3:
        print("acesso negado,{} não é um termo valido".format(ge))
        exit()
    else:
        count += 1

lista_m = ["luiz".upper(), "joao".upper(), "renato".upper()]
lista_f = ["julia".upper(), "mariana".upper(), "sara".upper()]
if ac == "USER" and ge == "HOMEM":
    us = input("digite o nome do usuario: ").upper()
    for x in lista_m:
        while x != us:
            us = input("'{}' não é um usuario valido, tente novamente: ".format(us)).upper()
            if count == 3:
                print("acesso negado,'{}' não é um usuario".format(us))
                exit()
            else:
                count += 1
        if x == us:
            print("Bem vindo usuario! {}".format(us))
            exit()
if ac == "USER" and ge == "MULHER":
    us = input("digite o nome do usuario: ").upper()
    for x in lista_f:
        while x != us:
            us = input("'{}' não é um usuario valido, tente novamente: ".format(us)).upper()
            if count == 3:
                print("acesso negado,'{}' não é um usuario".format(us))
                exit()
            else:
                count += 1
        if x == us:
            print("Bem vindo usuaria! {}".format(us))  
            exit()
listad_m = ["dmitry".upper(), "marcos".upper(), "carl".upper()]
listad_f = ["jujuzin".upper(), "elian".upper(), "artorias".upper()]
if ac == "ADM" and ge == "HOMEM":
    ad = input("digite o nome do administrador: ").upper()
    for x in listad_m:
        while x != ad :
            ad = input("'{}' não é um administrador valido, tente novamente: ".format(ad)).upper()
            if count == 3:
                print("acesso negado,'{}' não é um administrador".format(ad))
                exit()
            else:
                count += 1
        if x == ad:
            print("Bem vindo administrador! {}".format(ad))
            exit()
if ac == "ADM" and ge == "MULHER":
    ad = input("digite o nome do administrador: ").upper()
    for x in listad_f:
        while x != ad:
            ad = input("'{}' não é um administrador valido, tente novamente: ".format(ad)).upper()
            if count == 3:
                print("acesso negado,'{}' não é um administrador".format(ad))
                exit()
            else:
                count += 1
        if x == ad:
            print("Bem vindo administradora! {}".format(ad))
            exit() 
exit()
