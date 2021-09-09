
item1= input("Adicione um item na lista: ")
item2= input("Adicione um item na lista: ")
item3= input("Adicione um item na lista: ")
item4= input("Adicione um item na lista: ")

lista = [item1, item2, item3, item4]

verificar = input("qual deseja verificar? ")

if verificar in lista:
    print("Sim, está na lista!")
else:
    print("Não está na lista")