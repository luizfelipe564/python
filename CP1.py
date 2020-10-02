from os import system, name 
from time import sleep 

def clear(): 
    if name == 'nt': 
        _ = system('cls') 
    else: 
        _ = system('clear') 
clear()
arq1 = input("Digite o nome do arquivo original: ")
arq2 = input("Digite o nome do arquivo que deseja verificar a integridade: ")


v1 = (open(arq1, 'rb').read())
v2 = (open(arq2, 'rb').read())

if v1 != v2:
    p = input(f"foi identificada uma alteração no arquivo {arq2}, deseja restaura-lo(s/n): ").upper()
    while p != "S" and p != "N":
        clear()
        print(f"foi identificada uma alteração no arquivo {arq2}, deseja restaura-lo(s/n): ")
        p = input(f"{p} invalido,tente(s/n): ").upper()
    if p == "S":        
        print("efetuando restauração")
        arquivo = open(arq1, 'r')
        conteudo = arquivo.readlines()
        arquivo = open(arq2, 'w') 
        arquivo.writelines(conteudo)
        arquivo.close()
        print("\ntudo pronto")
        print("\nencerrando programa")
        sleep(6)
        clear()
        exit()
    elif p == "N":
        clear()
        print("encerrando programa")
        sleep(3)
        exit()
else:
    clear()
    print(f"Arquivo {arq2} esta integro")
    sleep(3)
    exit()
