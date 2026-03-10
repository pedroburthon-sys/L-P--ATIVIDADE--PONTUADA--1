import os
os.system('cls || clear')

print('Insira o nome do produto que deseja comprar:')
nome_produto = input().lower()
print('Insira a quantidade do produto que deseja comprar:')
quantidade_produto = int(input())


detergente = 2.50
sabonete = 3.00
esponja = 1.50

match nome_produto:
    case "detergente":
        valor_total = quantidade_produto * detergente
    case "sabonete":
        valor_total = quantidade_produto * sabonete
    case "esponja":
        valor_total = quantidade_produto * esponja
    case _:
        print("Produto inválido.")
        exit()
        
if quantidade_produto <= 5:
    valor_total = valor_total * 0.98
elif quantidade_produto >5 and quantidade_produto <= 10:
    valor_total = valor_total * 0.97
elif quantidade_produto > 10:
    valor_total = valor_total * 0.95
    
print(f'\nO valor total a ser pago é R$ {valor_total:.2f}')