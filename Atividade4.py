#Elabore um programa em Python que leia as duas notas de prova (P1 e P2) e duas notas de trabalho (T1 e T2) e posteriormente exiba a mensagem ‘Aprovado’ ou ‘Não aprovado’ dependendo dos valores obtidos, conforme as regras de cálculo definidas a seguir:
#• Média de provas: MP = (P1 + P2)/2
#• Média de trabalhos: MT = (T1 + T2)/2
#• Média final: MF = 0,8MP + 0,2MT
#• Situação:
#◦ Se MF ≥ 6,0 → aprovado
#◦ Se MF < 6,0 → não aprovado

p1 = float(input("Informe o valor da nota obtida na prova 1: "))
p2 = float(input("Informe o valor da nota obtida na prova 2: "))
t1 = float(input("Informe o valor obtido no trabalho 1: "))
t2 = float(input("Informe o valor obtido no trabalho 2: "))
MP = (p1 + p2) / 2 # Média das provas
MT = (t1 + t2) / 2 # Média dos trabalhos
MF = (0.8 * MP) + (0.2 * MT) # Média final ponderada
print(f"O valor da média final é de: {MF:.2f}")

if MF >= 6.0: 
  print("Aprovado")
else:
 print("Não aprovado")
