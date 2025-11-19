
pedido1 = "1 - Macarrão - R$ 23,99"
pedido2 = "2 - Arroz e Feijão - R$ 15,00"
pedido3 = "3 - Pizza Italiana - R$ 29,99"
pedido4 = "5 - Ratatuile - R$ 9,99"
resuPedidos = ["Nada", "Macarrão", "Arroz e Feijão", "Pizza Italiana", "Ratatuile"]
QuantidadeComida = 0

bebida1 = "1 - Suco de laranja - R$ 1,99"
bebida2 = "2 - Coca Cola Zero - R$ 5,00"
bebida3 = "3 - Coca Cola Normal - R$ 5,50"
bebida4 = "4 - Fanta Uva - R$ 2,99"
resuBebidas = ["Nada", "Suco de laranja", "Coca Cola Zero", "Coca Cola Normal", "Fanta Uva"]
QuantidadeBebida = 0

sobremesa1 = "1 - Bolo de Coco - R$ 9,99"
sobremesa2 = "2 - Páve - R$ 9,99"
sobremesa3 = "3 - Salada de Frutas - R$ 5,99"
sobremesa4 = "4 - Pudin - R$ 4,99"
resuSobremesa = ["Nada", "Bolo de Coco", "Páve", "Salada de Frutas", "Pudin"]
QuantidadeSobremesa = 0

resp = ""

comida = ""
bebida = ""
sobremesa = ""

total = 0.00
print("Seja bem vindo a |Fazbear Restarant's|\n\nGostaria de ver o menu? Sim/Não") #Menu
respPergunta = str(input("Responda: ")) # Comida
if respPergunta == "Sim" or respPergunta == "sim":
    print(pedido1, pedido2, pedido3, pedido4, sep="\n")
    resp = int(input("Qual vc gostaria de pedir? "))
    
    if resp == 1:
        comida = pedido1
        print("\n Comida: (",resuPedidos[resp],")")
        QuantidadeComida = int(input("Quantidade: "))
        
        total = total + 23.99 * QuantidadeComida
    elif resp == 2:
        comida = pedido2
        print("\n Comida: (",resuPedidos[resp],")")
        QuantidadeComida = int(input("Quantidade: "))
        
        total = total + 15.00 * QuantidadeComida
    elif resp == 3:
        comida = pedido3
        print("\n Comida: (",resuPedidos[resp],")")
        QuantidadeComida = int(input("Quantidade: "))
        
        total = total + 29.99 * QuantidadeComida
    elif resp == 4:
        comida = pedido4
        print("\n Comida: (",resuPedidos[resp],")")
        QuantidadeComida = int(input("Quantidade: "))
        
        total = total + 9.99 * QuantidadeComida
    else:
        print("Nada foi selecionado")

    print("\nGostaria de uma bebida? Sim/Não ") # Bebida
    respPergunta = str(input("Responda: "))

    if respPergunta == "Sim" or respPergunta == "sim":
        print(bebida1, bebida2, bebida3, bebida4, sep="\n")
        print("Qual bebida vc quer?")
        respBebida = int(input("Bebida: "))
        
        
        if respBebida == 1:
            bebida = bebida1
            print("\n Comida: ("x",QuantidadeComida,"",resuPedidos[resp],")\n Bebida: (",resuBebidas[respBebida],")\n")
            QuantidadeBebida = int(input("Quantidade: "))
            
            total = total + 1.99
        elif respBebida == 2:
            bebida = bebida2
            print("\n Comida: (",resuPedidos[resp],")\n Bebida: (",resuBebidas[respBebida],")\n")
            QuantidadeBebida = int(input("Quantidade: "))
            
            total = total + 5.00
        elif respBebida == 3:
            bebida = bebida3
            print("\n Comida: (",resuPedidos[resp],")\n Bebida: (",resuBebidas[respBebida],")\n")
            QuantidadeBebida = int(input("Quantidade: "))
            
            total = total + 5.50
        elif respBebida == 4:
            bebida = bebida4
            print("\n Comida: (",resuPedidos[resp],")\n Bebida: (",resuBebidas[respBebida],")\n")
            QuantidadeBebida = int(input("Quantidade: "))
            
            total = total + 2.99
        else:
            print("Nada foi selecionado\n")

    else:
        print("Ok")
    print("\n\nGostaria de uma sobremesa? Sim/Não") #Sobremesa
    respPergunta = str(input("Responda: "))

    if respPergunta == "Sim" or respPergunta == "sim":
        print(sobremesa1, sobremesa2, sobremesa3, sobremesa4, sep="\n")
        print("Qual Sobremesa vc quer?")
        respSobremesa = int(input("Sobremesa: "))
        
        
        if respSobremesa == 1:
             sobremesa = sobremesa1
             print("\n Comida: (",resuPedidos[resp],")\n Bebida: (",resuBebidas[respBebida],")\n Sobremesa: (",resuSobremesa[respSobremesa],")")
             QuantidadeSobremesa = int(input("Quantidade: "))
             
             total = total + 9.99 * QuantidadeSobremesa
        elif respSobremesa == 2:
             sobremesa = sobremesa2
             print("\n Comida: (",resuPedidos[resp],")\n Bebida: (",resuBebidas[respBebida],")\n Sobremesa: (",resuSobremesa[respSobremesa],")")
             QuantidadeSobremesa = int(input("Quantidade: "))
             
             total = total + 9.99 * QuantidadeSobremesa
        elif respSobremesa == 3:
             sobremesa = sobremesa3
             print("\n Comida: (",resuPedidos[resp],")\n Bebida: (",resuBebidas[respBebida],")\n Sobremesa: (",resuSobremesa[respSobremesa],")")
             QuantidadeSobremesa = int(input("Quantidade: "))
             
             total = total + 5.99 * QuantidadeSobremesa
        elif respSobremesa == 4:
             sobremesa = sobremesa4
             print("\n Comida: (",resuPedidos[resp],")\n Bebida: (",resuBebidas[respBebida],")\n Sobremesa: (",resuSobremesa[respSobremesa],")")
             QuantidadeSobremesa = int(input("Quantidade: "))
             
             total = total + 4.99 * QuantidadeSobremesa
        else:
             print("Nada foi selecionado")

    else:
        print("Ok")

    print("\n\nGostaria de fechar o pedido? Sim/Não ") # Pagamento
    respPergunta = str(input("Responda: "))

    if respPergunta == "Sim":
        print(comida, bebida, sobremesa,sep="\n")
        print("\nTotal = R$:",total)
    else:
        print("\nO total foi: ",total)
        print("Seu peedido jaja vai chegar :)")

    print("\n\nQual seria sua forma de pagamento?\nPix\nDinheiro\nCartão\n")
    respPergunta = str(input("Escolha: "))
    if respPergunta == "Pix":
        print("R$:",total," no Pix")
    elif respPergunta == "Dinheiro":
        print("R$:",total," no Dinheiro vivo")
    elif respPergunta == "Cartão":
        print("\n\nCredito ou Debito?")
        respPergunta = str(input("Qual? "))
        if respPergunta == "Credito":
            print("R$:",total," no Credito")
        else:
            print("R$:",total," no Debito")
    else:
        print("Pague ou morra!")
              
    
    
else:
    print("Ok, tenha um otimo dia :)")

