#listas em Python []
frutas = ["Banana","Laranja","Maçã","Manga"]
print(frutas)
#Mostrando apenas um elemento da lista
print(frutas[3])
#Incluindo elemento na lista 
frutas.append("Mexerica")
print(frutas)
#Retirando elemento da lista
frutas.remove("Banana")
print(frutas)
#pop: apresenta o elemento que foi declarado sua posição e retira-o
ultima = frutas.pop()
penultima = frutas.pop(2)
antepenultima = frutas.pop(1)
primeira = frutas.pop(0)
print(ultima)
print(penultima)
print(antepenultima)
print(primeira)
print(frutas)
#acrescenta elementos na posição declarada
frutas.insert(0,"Mamão")
frutas.insert(1,"Morango")
frutas.insert(2,"Kiwi")
frutas.insert(3,"Pitaya")
frutas.insert(4,"Carambola")
frutas.insert(5,"Caqui")
frutas.insert(6,"Uva")
print(frutas)
#mostra a lista de trás pra frente 
frutas.reverse()
print(frutas)
#fala quantos itens há na lista 
print(len(frutas))
print(frutas)
#Embaralha os itens da lista
frutas.sort()
print(frutas)




frutas.insert(0, "Romã")
print(frutas)
# ==================================DESAFIO================================================
# Você vai criar um programa que gerencia uma lista de tarefas.
#  O programa deve:
# 1. Permitir que o usuário adicione tarefas. Cada tarefa deve ter: Descrição (string),       Prioridade (inteiro de 1 a 5, onde 1 é a prioridade mais alta) e Status (inicialmente “pendente”);
# 2. Armazenar cada tarefa como um dicionário com as chaves "descrição", "prioridade" e "status";
# 3. Manter todas as tarefas numa lista;
# 4. Criar funções para: Adicionar tarefas, Mostrar todas as tarefas ordenadas por prioridade (da maior para a menor) e Marcar uma tarefa como concluída (alterar o status para “concluída”);
# 5. Criar uma função main() que permita ao usuário escolher opções num menu para: Adicionar tarefa, Listar tarefas, Marcar tarefa como concluída e Sair do programa.


#=========FAZENDOOO=========
#O PROGRAMA É UMA LISTA, ONDE O USUÁRIO PODERÁ:
#•ADICIONAR ITENS À LISTA 
#•MOSTRAR TODAS AS TAREFAS
#•VER SUA PRIORIADE (1 A 5)
#•MARCAR O STATUS DELA (PENDENTE OU CONCLUÍDA)
