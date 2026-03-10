import os 
os.system('cls || clear')

print('Informe a quantidade em Kg de moragos comprados:')
quantidade_morangos = float(input())
print('Informe a quantidade em Kg de maçãs compradas:')
quantidade_macas = float(input())

valor_morango = 2.50
valor_macas = 1.80

if quantidade_morangos >= 5 or quantidade_macas >= 5:
    valor_morango = 2.20
    valor_maca = 1.50

preco = (quantidade_morangos * valor_morango) + (quantidade_macas * valor_macas)
if quantidade_macas + quantidade_morangos > 10 or preco > 15:
    preco = preco * 0.9

print(f"O valor total a ser pago é R$ {preco}")