# Crie um programa que peça ao usuário o nome de um aluno e as três notas que ele obteve em uma disciplina, junto com o peso de cada uma dessas notas (ou seja, a importância de cada nota na média final). O programa deve calcular a média ponderada do aluno e exibir o resultado com uma mensagem personalizada.



# Pedindo nome do aluno ao usuário
nome = input("Escreva o nome do(a) aluno(a): ")

# Pedindo o valor da nota 1 e o peso dela
n1 = float(input(f"Escreva quanto {nome} obteve de Nota 1: "))
p1 = float(input("Informe o peso dessa nota: "))
# Pedindo o valor da nota 2 e o peso dela
n2 = float(input(f"Escreva quanto {nome} obteve de Nota 2: "))
p2 = float(input("Informe o peso dessa nota: "))
# Pedindo o valor da nota 3 e o peso dela
n3 = float(input(f"Escreva quanto {nome} obteve de Nota 3: "))
p3 = float(input("Informe o peso dessa nota: "))
 
# Calculando o valor da média ponderada
media_ponderada = (n1 * p1 + n2 * p2 + n3 * p3) / (p1 + p2 + p3)

# Informando ao usuário valor da média pondera obtido pelo aluno através dos valores informados

print(f"O(A) aluno(a) {nome}, obteve de média pondera o valor de: {media_ponderada:.2f}")