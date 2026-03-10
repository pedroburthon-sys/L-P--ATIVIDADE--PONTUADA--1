import os
os.system("cls || clear")

# limpa o terminal

nome= input(" Digite seu nome:")
sexo= input(" Digite seu sexo:").lower()
estado= input(" Digite seu estado civil:").lower()

if sexo == "feminino" and estado == "casada":
    
   tempo = input(" Diga o tempo de casada:")