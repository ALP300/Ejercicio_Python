#La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. 
# Los ingredientes para cada tipo de pizza aparecen a continuación.
#Ingredientes vegetarianos: Pimiento y tofu.
#Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
#Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y 
# en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija.
# Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas.
# Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes
# que lleva.

print("Bienvenidos a la mejor pizzería: Bella Napoli. \nTipos de pizzas:\n\t1- Vegetariana\n\t2- No Vegetariana")
tipo= input("Introduce el número de correspondiente a la pizza que deseas pedir: ")
if tipo=="1":
    print("Ingredientes de pizzas vegetarianas\n\t1- Pimiento\n\t2- Tofu\n ")
    ingrediente= input("Introduce el ingrediente que deseas: ")
    print("Pizza vegetariana con mozzarella, tomate y ", end="")
    if ingrediente=="1":
        print("pimiento")
    else:
        print("tofu")
else:
    print("Ingredientes de pizzas no vegetarianas\n\t1- Peperoni\n\t2- Jamón\n\t3- Salmón ")
    ingrediente= input("Introduce el ingrediente que deseas: ")
    print("Pizza no vegetariana con mozzarella, tomate y ", end="")
    if ingrediente=="1":
        print("peperoni")
    elif ingrediente=="2":
        print("jamón")
    else:
        print("salmón")
    