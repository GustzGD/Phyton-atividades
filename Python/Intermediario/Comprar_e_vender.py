while True:

    item = str(input("Item: "))
    quantidade = int(input("Quantidade: "))
    valor = float(input("Preço: "))


    def vender(qtdade, preco, itemN):
        print("Você vai ganhar R$:",qtdade * preco," com (",itemN,")")

    def comprar(qtdade, preco, itemN):
        print("Total gasto com (",itemN,") foi R$:",qtdade * preco)

    resp = int(input("(1 = Comprar) (2 = Vender)\n"))


    if resp == 1:
        comprar(qtdade = quantidade, preco = valor, itemN = item)
    elif resp == 2:
        vender(qtdade = quantidade, preco = valor, itemN = item)

    ipt = input("Aperte Enter para repetir!")


