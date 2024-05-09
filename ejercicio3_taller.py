#Escribe un programa que solicite al usuario un número entero y calcule 
#si es divisible por 3 y por 5. 

numero= int(input("Introduce un número entero: "))

if numero%3==0 and numero%5==0:
    print("El número es divible por 3 y 5")
else:
    print("El número no es divisible por 3 ni por 5")