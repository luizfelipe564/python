from os import system, name 
from time import sleep 
import hashlib

def clear(): 
    if name == 'nt': 
        _ = system('cls') 
    else: 
        _ = system('clear') 
clear()
arq1 = input("Digite o nome do arquivo original: ")
arq2 = input("Digite o nome do arquivo que deseja verificar a integridade: ")

hash0 = hashlib.new('ripemd160')
hash0.update(open(arq1, 'rb').read())

hash1 = hashlib.new('ripemd160')
hash1.update(open(arq2, 'rb').read())

if hash0.digest() != hash1.digest():
    p = input(f"foi identificada uma alteração no arquivo {arq2}, deseja restaura-lo(s/n): ").upper()
    while p != "S" and p != "N":
        clear()
        print(f"foi identificada uma alteração no arquivo {arq2}, deseja restaura-lo(s/n): ")
        p = input(f"{p} invalido,tente(s/n): ").upper()
    if p == "S":        
        print("efetuando restauração")
        arquivo = open(arq1, 'r') # Abra o arquivo (leitura)
        conteudo = arquivo.readlines()
        arquivo = open(arq2, 'w') # Abre novamente o arquivo (escrita)
        arquivo.writelines(conteudo)    # escreva o conteúdo criado anteriormente nele.
        arquivo.close()
        print("\ntudo pronto")
        print("\nencerrando programa")
        sleep(2)
        clear()
        exit()
    elif p == "N":
        clear()
        print("encerrando programa")
        sleep(2)
        exit()
else:
    clear()
    print(f"Arquivo {arq2} esta integro")
    sleep(2)
    exit()
