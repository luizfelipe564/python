graduacao = input("que tipo de graduação voce realiza: ").upper()
while graduacao != "TECNOLOGO" and graduacao != "BACHARELADO":
    graduacao = input ("digite uma graduação valida: ").upper()
if graduacao == "TECNOLOGO":
        print("2 a 3 anos")

else :
    print("4 até 6 anos")
