comidas = ["Nada","Pizza de peperone","Pizza 7 queijos","Pizza de calabresa","Pizza do Freddy (Cogumelos)","Pizza da Chica (Frango)","Pizza do Bonnie (Strogonoffe)","Pizza do Foxy (Frutos do Mar)","Pizza 87 (Supresa de 1987!)"]
precoComida = [0., 25., 25., 15., 30., 30., 30., 30., 50.]

bebidas = ["Nada","Fazbear Cola","Chica’s Citrus Punch","Bonnie Berry Blast ","Foxxy Fizz","Golden Grape Soda","Night Guard Energy Drink","Balloon Boy Bubble Tea","Pizza Shake"]
precoBebida = [ 0., 6.50, 7., 6., 6.5, 8., 9., 8., 10.]

sobremesas = ["Nada","Pudin","Pizza de chocolate com morango","Salada de Frutas","Bolinhos da Chica","Bolo Golden"]
precoSobremesa = [ 0., 4.50, 25., 5., 10.50, 15.]

formasPagamento = ["Pix","Cheque","Dinheiro vivo","Cartão"]

totalPedido = 0.

print("============[ Bem vindo a Freddy Fazbear's Pizzaria ]====================\n")
respInicio = str(input("Gostaria de ver nosso menu? (Sim/Não): "))



if respInicio == "Sim" or respInicio == "sim" or respSobremesa == "s":
    print("\n=====================================================================")
    for i in range(len(comidas)):
        print(f"{i} - {comidas[i]} - R$: {precoComida[i]:.2f}")
    print("\n=====================================================================")
else:
    print("Tchau, até a proxima!")
    enter = input()

while respInicio == "Sim" or respInicio == "sim" or respSobremesa == "s":
    
    ########
    
    print("\nQual pizza você deseja?") #Pedindo Pizza
    pizzaEsc = int(input("\nNúmero da pizza: "))
    

    if pizzaEsc >= len(comidas):
        pizzaEsc = 0

    totalPedido = totalPedido + precoComida[pizzaEsc]
    print("\n================[ Pedido do cliente ]================")
    print("\n  Pizza: (",comidas[pizzaEsc],")")
    print("\n=====================================================")
    
    ########
    
    print("\nGostaria de ver o menu de Bebidas?") #Pedindo Bebida
    respBebida = str(input("(Sim/Não): "))

    if respBebida == "Sim" or respBebida == "sim" or respSobremesa == "s":
        print("\n/=====================================================================\")
        for i in range(len(bebidas)):
             print(f"{i} - {bebidas[i]} - R$: {precoBebida[i]:.2f}")

        print("\n\=====================================================================/")

        bebidaEsc = int(input("\nColoque o número da bebida: "))
        
        if bebidaEsc >= len(bebidas):
            bebidaEsc = 0

        totalPedido = totalPedido + precoBebida[bebidaEsc]
        
        print("\n================[ Pedido do cliente ]================")
        print("\n  Pizza: (",comidas[pizzaEsc],")\n  Bebida: (",bebidas[bebidaEsc],")")
        print("\n=====================================================")
    else:
        print("\nOk.\n")

    ########

    print("\nGostaria de ver o munu de sobremesas?") #Sobremesa
    respSobremesa = str(input("(Sim/Não): "))

    if respSobremesa == "Sim" or respSobremesa == "sim" or respSobremesa == "s":
        print("\n=====================================================================")
        for i in range(len(sobremesas)):
            print(f"{i} - {sobremesas[i]} - R$: {precoSobremesa[i]:.2f}")
        print("\n=====================================================================")

        sobremesaEsc = int(input("\nColoque o número da sobremesas: "))
        totalPedido = totalPedido + precoSobremesa[sobremesaEsc]
         
        if sobremesaEsc >= len(sobremesas):
            sobremesaEsc = 0
            

    else:
        print("\nOk.\n")
    print("\n================[ Pedido do cliente ]================")
    print("\n  Pizza: (",comidas[pizzaEsc],")\n  Bebida: (",bebidas[bebidaEsc],")\n  Sobremesas: (",sobremesas[sobremesaEsc],")")
    print("\n=====================================================")
    print("\nTotal foi de R$: ",totalPedido)

    print("\nQual seria a forma de pagamento? \n")
    for i in range(len(formasPagamento)):
        print(f"{i} - {formasPagamento[i]}")
        
    respForma = int(input("Número da forma de pagamento: "))
    
    print(f"Ok. R$:{totalPedido:.2f} no {formasPagamento[respForma]}")
    
    enter = input()
    break
        
        
    
    
    

    

    

    


