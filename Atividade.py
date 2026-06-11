# O custo ao consumidor de um carro novo é a soma do custo de fábrica com a porcentagem do distribuidor e dos impostos (aplicados ao custo de fábrica). Supondo que a porcentagem do distribuidor seja de 12% do preço de fábrica e os impostos de 30% do preço de fábrica, fazer um programa em Python para ler o custo de fábrica de um carro e imprimir o custo ao consumidor.

custo_fabrica = float(input("Escreva o valor de custo de fábrica do carro: "))
distribuidor = custo_fabrica * 0.12
impostos = custo_fabrica * 0.30
custo_consumidor = custo_fabrica + distribuidor + impostos 

print(f"O custo ao consumidor é de: {custo_consumidor}")