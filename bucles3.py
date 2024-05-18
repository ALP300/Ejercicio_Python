# BUCLES
# FOR, WHILE, DO-WHILE

#CONDICIONALES
# IF, SWITCH

#1-10
for i in range(1,11):
    print(i)

#Escribir un programa que pida al usuario un número entero positivo 
# y muestre por pantalla todos los números impares desde 1 hasta 
# ese número separados por comas.  #20
n= int(input("Introduce un número entero positivo: "))  
for i in range(1,n+1,2):
    print(i, end=",")

