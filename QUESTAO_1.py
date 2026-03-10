import os 

# Limpar o terminal
os.system("cls || clear")

print("=== Comparação de soma ===")


         # solicitando dados 
         
numero_A = int(input("Digite um numero:"))
numero_B = int(input("Digite um numero:"))
numero_C = int(input("Digite um numero:"))
 
 # calcule
soma = numero_A + numero_B
 
 # processando dados
if soma < numero_C:
     print("A soma de A+B é MENOR")
elif soma > numero_C:
     print("A soma de A+B é MAIOR")