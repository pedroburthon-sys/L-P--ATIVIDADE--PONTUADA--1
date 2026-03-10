import os
os.system('cls || clear)')

print('Digite o nome do aluno:')
nome = input()
print('\nDigite a primeira nota do aluno:')
nota1 = float(input(''))
print('\nDigite a segunda nota do aluno:')
nota2 = float(input(''))
print('\n')

media = (nota1 + nota2) / 2
if media >= 6:
     print(f'Parabéns, o {nome} foi aprovado')
elif media >= 4:
    print(f'Infelizmente {nome} está de recuperação')       
elif media < 4:
    print(f'Infelizmente {nome} foi reprovado\n')