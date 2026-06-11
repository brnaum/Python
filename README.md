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
