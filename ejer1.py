#Crea un programa que pida al usuario ingresar un número del 1 al 7, e imprima el día de la semana 
# correspondiente. Si el número está fuera de ese rango, mostrar un mensaje de error.
num= int(input("Ingrese un número del 1 al 7: "))  #4
dias_semana={
    1:"Lunes",
    2:"Martes",
    3:"Miercoles",
    4:"Jueves",
    5:"Viernes",
    6:"Sábado",
    7:"Domingo"
}
if num in dias_semana:
    print("El día correspondiente es: ", dias_semana[num])
else:
    print("Número no se encuentra en el rango")