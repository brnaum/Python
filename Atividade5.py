#Faça um programa em Python que leia a temperatura em graus Celsius determine a classificação da temperatura:
#• Menor que 0°C: Frio extremo 
#• De 0°C a 10°C: Frio
#• De 11°C a 25°C: Ameno
#• De 26°C a 35°C: Quente
#• Maior que 35°C: Muito quente

temperatura = float(input("Informe a temperatura em °C: "))
if temperatura < 0:
  print("Frio extremo")
elif temperatura <= 10:
  print("Frio")
elif temperatura <= 25:
  print("Ameno")
elif temperatura <= 35:
  print("Quente")
else:
  print("Muito quente")