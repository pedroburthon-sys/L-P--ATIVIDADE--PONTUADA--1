import os
os.system('cls || clear')

print('Digite a cor do CD desejada:')
cor_cd = input().lower()
print('Digite a quantidade de CDs desejada:')
quantidade_cds = int(input())

verde = 10
azul = 20
amarelo = 30
vermelho = 40

match cor_cd:
    case 'verde':
        valor_cd = verde * quantidade_cds
    case 'azul':
        valor_cd = azul *  quantidade_cds
    case 'amarelo':
        valor_cd = amarelo * quantidade_cds
    case 'vermelho':
        valor_cd = vermelho * quantidade_cds
    case _:
        print('Cor de CD inválida.')
        exit()
        
print(f'\nO valor total a ser pago é R$ {valor_cd:.2f}')