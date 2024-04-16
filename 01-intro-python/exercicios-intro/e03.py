#entrada:  valor de uma compra 
# saída: valor final com desconto e o desconto aplicado com base nas regras:

#COMPRAS ENTRE R$0,01 e R$9,99 - 0% de desconto
#COMPRAS ENTRE R$10,00 e R$99,99 - 5% de desconto
#COMPRAS ENTRE R$100,00 e R$499,99 - 10% de desconto
#COMPRAS IGUAIS OU SUPERIORES A R$500,00 - 15% de desconto


valor = float (input ("digite o valor da sua compra\n"))


if valor >= 10.00 and valor <= 99.99:
    valoratual = valor - (valor * 0.05)
    print ("você conseguiu 5 por cento de desconto e seu valor a pagar é R$", valoratual)
elif valor >= 100.00 and valor <= 499.99:
    valoratual = valor - (valor * 0.1)
    print ("você conseguiu 10 por cento de desconto e seu valor a pagar é R$", valoratual)
elif valor >= 500.00:
    valoratual = valor - (valor * 0.15)
    print ("você conseguiu 15 por cento de desconto e seu valor a pagar é R$", valoratual)
else:
    print ("você não tem desconto e seu valor a pagar é R$", valor)
