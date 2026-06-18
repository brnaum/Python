# . Faça um programa em Python que simula as operações de 
# um banco. O programa deve apresentar um menu com as 
# seguintes opções:
# 1. Depositar (O programa deve pedir o valor a ser 
# depositado e somá-lo ao saldo)
# 2. Sacar (O programa deve pedir o valor a ser sacado e 
# subtrair do saldo, desde que o valor seja menor ou igual 
# ao saldo disponível)
# 3. Consultar Saldo (O programa deve exibir o saldo 
# atual)
# 4. Sair (O programa termina)
# O programa deve manter um saldo inicial de R$ 1000,00 
# e permitir ao usuário realizar depósitos e saques até que 
# ele escolha a opção "Sair".

print("=======BANCO=======")
saldo_inicial = 1000
saldo_inicial = print("Seu saldo atual é de R$1000,00 ")
print("1. Depositar")
print("2. Sacar")
print("3. Consultar Saldo")
print("4. Sair")
opcoes = int(input("Escolha uma das opções: "))
if opcoes == 1:
    deposito = float(input("Qual é o valor que deseja depositar: "))
    soma = saldo_inicial + deposito 
    print(f"Seu saldo é de: {soma}")