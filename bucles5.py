#Escribir un programa en el que se pregunte al usuario por una frase y una letra,
# y muestre por pantalla el número de veces que aparece la letra en la frase.

frase= input("Introduce una frase: ") #Hola amigos
letra= input("Introduce una letra: ") #a 
contador=0

fraseMinuscula= frase.lower()
print(contador)

for i in frase:  #H
    if i==letra:
        contador+=1
print("la letra",letra,"aparece", contador, "en la frase: ",frase)
print("La letra '%s' aparece %2i veces en la frase '%s'." % (letra,contador,frase))

print(contador)