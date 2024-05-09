import math
#Escribe un programa que solicite al usuario un número entero y calcule 
#su cuadrado y su cubo. 
numero= int(input("Introduce un número entero: "))
cuadrado= numero**2
cubo= math.pow(numero,3)

print("El cuadrado del número es: ",cuadrado)
print("El cubo del número es: ",cubo)