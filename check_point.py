count = 0
listae=["luiz2203@gmail.com", "renato06@outlook.com", "magalhães1990@live.com", "zbrjr@gmail.com", "manezingameplay@outlook.com", "julioulio2020@live.com", "marcondessilva@gmail.com", "totoro23@outlook.com", "mariogames@live.com", "ricagames@gmail.com"]
listac1=["4929114884242016", "4024007125426055", "4860417975388174818"]
listac2=["2221000966488552", "2221006626059253", "2720993222202898"]
listac3=["370252601210973", "379714718751778", "342836578416061"]
listac4=["36092008586153" "36580673795398", "36064149200861"]
listacpf=["680.674.400-18", "820.554.410-78", "620.384.930-81", "505.432.680-47", "831.346.820-36", "128.957.000-01", "811.823.260-30", "729.761.920-57"]

while True:
    print("________________________________________________VAZAMENT.IO________________________________________________")
    print("EMAILS VAZADOS____________________________________________________________________________________________1")
    print("CARTOES VAZADOS___________________________________________________________________________________________2")
    print("CPF_______________________________________________________________________________________________________3")
    print("SAIR______________________________________________________________________________________________________4")
    cliente = input("Digite o numero a direita da  informação deseja buscar: ")
    while cliente != "1" and cliente != "2" and cliente != "3" and cliente != "4":
        cliente = input("Comando {} invalido, digite novamente: ".format(cliente))
        if count == 2:
            break
        else:
            count += 1
    if cliente == "1" :
        capturae = input("digite o email que deseja pesquisar: ")
        for x in listae:
            if x == capturae:
                print("o email {} esta na lista , suas informacoes podem ter vazado".format(capturae))
                
                break
            else:
                print("nao esta na lista")
                
    if cliente == "2":
        print("________________________________________________VAZAMENT.IO________________________________________________")
        print("___________________________________________________VISA____________________________________________________")
        print("________________________________________________Mastercard_________________________________________________")
        print("___________________________________________________AMEX____________________________________________________")
        print("__________________________________________________Dinners__________________________________________________")
        marca = input("qual a marca de cartao que deseja pesquisar: ").upper()
        while marca != "VISA" and marca != "Mastercard" and marca != "AMEX" and marca != "Dinners":
            marca = input(" marca {} nao consta , verifique e digite novamente: ".format(marca)).upper()
            if count == 2:
                print("A marca {} nao consta na lista de vazamentos!".format(marca))
                break
            else:
                count += 1
        if marca == "VISA":
            ncard1 = input("digite o numero do cartao {} desejado(ex:4860417975388174818):".format(marca))
            for x in listac1:
                if x == ncard1:
                    print("o cartao {} foi vazado".format(ncard1))
                else:
                    print("sem registro de vazamentos no cartao {}".format(ncard1))
        if marca == "Mastercard":
            ncard2 = input("digite o numero do cartao {} desejado(ex:2720993222202898):".format(marca))
            for x in listac2:
                if x == ncard2:
                    print("o cartao {} foi vazado".format(ncard2))
                else:
                    print("sem registro de vazamentos no cartao {}".format(ncard2))
        if marca == "AMEX":
            ncard3 = input("digite o numero do cartao {} desejado(ex:370252601210973):".format(marca))
            for x in listac3:
                if x == ncard3:
                    print("o cartao {} foi vazado".format(ncard3))    
                else:
                    print("sem registro de vazamentos no cartao {}".format(ncard3))
        if marca == "Dinners":
            ncard4 = input("digite o numero do cartao {} desejado(ex:370252601210973):".format(marca))
            for x in listac4:
                if x == ncard4:
                    print("o cartao {} foi vazado".format(ncard4))
                else:
                    print("sem registro de vazamentos no cartao {}".format(ncard4))
    if cliente == "3" :
        cpf = input("digite o cpf que deseja pesquisar: ")
        for x in listacpf:
            if x == cpf:
                print("o CPF {} esta na lista , suas informacoes podem ter vazado".format(cpf))
                break
            else:
                print("nao esta na lista")
    if cliente == "4" :
        exit()
    
