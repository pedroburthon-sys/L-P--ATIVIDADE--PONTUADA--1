import os
os.system('cls || clear')

print('Informe a sua renda mensal')
renda = float(input())
print('Informe o valor do empréstimo desejado')
emprestimo_desejado = float(input())
print('Informe o número de parcelas desejado')
parcelas = int(input())
parcelas_valor = emprestimo_desejado / parcelas

if emprestimo_desejado > (renda * 10) or parcelas > (renda * 0.3):
    print('\nEmpréstimo negado.')
else:
    print('\nEmpréstimo aprovado.')