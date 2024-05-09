#Escribe un programa que solicite al usuario dos números y muestre su
#suma, resta, multiplicación, división, división entera y residuo (módulo).
numero1 = float(input("Introduce el primer número: "))
numero2 = float(input("Introduce el segundo número: "))
suma= numero1+numero2
resta= numero1-numero2
multiplicacion= numero1*numero2
division= numero1/numero2
division1= numero1//numero2
modulo= numero1%numero2
print("La suma es: ",suma)
print("La resta es: ",resta)
print("La multiplicación es: ",multiplicacion)
print("La división es: ",division)
print("La división entera es: ",division1)
print("El módulo es: ",modulo)