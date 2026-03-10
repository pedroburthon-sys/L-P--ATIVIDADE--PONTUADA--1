import os

# Limpar o terminal
os.system("cls || clear")

print("=== Comparação ===")
# solicitando dados 
         
numero_A = int(input("Digite um numero:"))
numero_B = int(input("Digite um numero:"))
# calcule

soma = numero_A + numero_B
multiplique = numero_A * numero_B

 # processando dados
if numero_A == numero_B:
     C= (soma)
else:
    C= multiplique
print("Resultado:" , C)
     