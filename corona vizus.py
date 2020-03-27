nome = input("nome do paciente: ")
idade = int (input("digite sua idade: "))

if idade < 15 or idade > 60:
    print( " procure acesso prioritario " )
    exit()

risco = input(",esta em grupo de risco sim ou não:").upper()

if risco != "SIM" and risco != "NAO":
    risco = input("digite apenas sim ou não: ").upper()

while risco == "SIM":
    print("procure acesso prioritario")

else:
    print("acesse a fila normal")
