#Solicita al usuario ingresar un número, lo divide por 10 y 
# muestra el resultado. Si el usuario ingresa algo que no puede 
# convertirse en un entero (ValueError) o intenta dividir por cero (ZeroDivisionError),
# el programa captura la excepción y muestra un mensaje de error adecuado.

try:
    num= int(input("Introduce un número: "))
    resultado= 10/num
    print("El resultado es: ",resultado)

except ValueError:
    print("ERROR: Debes introducir un número válido")
except ZeroDivisionError:
    print("El resultado no se puede dividir por cero. ")