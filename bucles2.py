palabra= input("Introduce una palabra: ") #Brinner
vocales=['a','e','i','o','u']
for vocal in vocales:
    repeticiones=0
    for letra in palabra:
        if letra==vocal:
            repeticiones+=1
        
    print("La vocal "+vocal+" aparece: "+str(repeticiones)+"veces")