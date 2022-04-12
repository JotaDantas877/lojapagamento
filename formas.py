print("{:=^40}".format(" BUDEGA STORE "))
preco = float(input("Preço total das compras: R$"))
print(''' Formas de pagamento:
1 - Á vista no dinheiro com 10% de desconto.
2 - Cartão de Debito.
3 - 2x ou mais no Cartão de Credito.
4 - 3x ou mais no Cartão de Credito.''')
opcao = int(input("Digite a forma de pagamento: "))


# valor a vista com desconto
if  opcao == 1:
    total = preco -(preco * 10 / 100)
elif opcao == 2:
    total  = preco 
    parcela = total / 2
# valor no cartão com juros
elif opcao == 3:
    total  = preco 
    parcela = preco / 2
    print("Sua compra  será pascelada em 2x vai custar R${:.2f} sem juros.".format(parcela))
elif opcao == 4:
    total  = preco + (preco * 20 / 100)
    totalparc = int(input("Favor informar a quantidade de parcelas:"))
    parcelas = total / totalparc
    print("Sua compra será parcelada em {}x de R${:.2f} com juros".format(totalparc, parcelas))
print("Sua compra de R${:.2f} vai custar R${:.2f} no total.".format(preco, total))

