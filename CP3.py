import math
def primo(p):
    while p == 1 :
        p = int(input("1 não é um primo valido por ser unidade, digite outro numero: \n"))
    while p > 2 and p % 2 == 0 :
        p = int(input(f"{p} não é primo, digite outro numero: \n"))
    divisor_maximo = math.floor(math.sqrt(p))
    for d in range (3, 1 + divisor_maximo, 2):
        while p % d == 0:
            p = int(input(f"{p} não é primo, digite outro numero: \n"))
p = int(input("digite um numero primo: \n"))
primo(p)
g = int (input("digite um numero qualquer"))
ca = int(input("para chave privada, digite um numero com no minimo 2 digitos:\n"))
cav = str(ca)
while len(cav) < 2:
    ca = int(input("numero baixo demais para chave privada, digite novamente\n"))
    cav = str(ca)
cb = int(input("para chave privada, digite um segundo numero com no minimo 2 digitos\n"))
cbv = str(cb)
while len(cbv) < 2:
    cb = int(input("numero baixo demais para chave privada, digite novamente\n"))
    cbv = str(cb)
cap = (p**ca)%g
cbp = p**cb%g

Sa = (cbp**ca)%g
Sb = (cap**cb)%g
print(f"{Sa}")
print(f"{Sb}")
if Sa == Sb :
    print("Houve comunicação entre os hosts")
    
