import os
os.system('cls || clear)')
print('Informe o tipo de combustível desejado (A - Álcool, G - Gasolina):')
tipo_combustivel = input().upper()
print('Informe a quantidade de litros desejada:')
quantidade_litros = float(input())

if tipo_combustivel == 'A':
    valor_litro = 3.79
    if quantidade_litros <= 25:
        desconto = 0.98
    else:
        desconto = 0.96
elif tipo_combustivel == 'G':
    valor_litro = 6.59
    if quantidade_litros <= 25:
        desconto = 0.97
    else:
        desconto = 0.95
        
preco = quantidade_litros * (valor_litro * desconto)
print(f'\nO valor total a ser pago é R$ {preco:.2f}\n\n\n')