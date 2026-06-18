# Crie um programa em Python que recebe um valor em reais e 
# o converte para outra moeda. Use um menu para escolher a 
# moeda de destino:
# 1. Dólar
# 2. Euro
# 3. Libra
# 4. Iene
# O programa deve perguntar o valor em reais e exibir o 
# valor convertido para a moeda escolhida. Use valores 
# fictícios para as taxas de conversão:
# 1 Real = 0.19 Dólar
# 1 Real = 0.17 Euro
# 1 Real = 0.15 Libra
# 1 Real = 25 Iene
valor_rs = float(input("Escreva o valor (em Reais) que deseja converter: "))
print("1. Dólar")
print("2. Euro")
print("3. Libra")
print("4. Iene")
moeda_destino = int(input("Escolha a moeda que deseja converter o valor (1 a 4): "))
if moeda_destino == 1:
    convertido = valor_rs * 0.19
    print(f"Valor em dólar: {convertido:.2f}")
elif moeda_destino == 2: 
    convertido = valor_rs * 0.17
    print(f"O valor em Euro: {convertido:.2f}")
elif moeda_destino == 3: 
    convertido = valor_rs * 0.15
    print(f"O valor em Libra: {convertido:.2f}")
elif moeda_destino == 4: 
    convertido = valor_rs * 25
    print(f"O valor em Iene: {convertido:.2f}")
else:
    print("Opção Inválida!")