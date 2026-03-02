# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc?t=5665

### Operadores Aritméticos ###

# Operaciones con enteros
print(3 + 4)
print(3 - 4)
print(3 * 4)
print(3 / 4)
print(10 % 3)   #Modulo (resto de la division)
print(10 // 3)  #Esto da siempre un numero int (lo aproxima)
print(2 ** 3)   #Elevar a algo
print(2 ** 3 + 3 - 7 / 1 // 4) #Se puede juntar

# Operaciones con cadenas de texto
print("Hola " + "Python " + "¿Qué tal?")
print("Hola " + str(5)) 
#Puedes forzar que el 5 seta de tipo str (como el del ejemplo) o ponerlo entre comillas

# Operaciones mixtas
print("Hola " * 5)        #Repetición de hola 5 veces
print("Hola " * (2 ** 3)) #Solo se puede con enteros

my_float = 2.5 * 2
print("Hola " * int(my_float))
#Esto daria un error porque estas multiplicando 2.5 * 2.0 por lo que te devuelve un tipo float

### Operadores Comparativos ###

# Operaciones con enteros
print(3 > 4)
print(3 < 4)
print(3 >= 4)
print(4 <= 4)
print(3 == 4) #Comparación de igualdad
print(3 != 4) #DIstinto

# Operaciones con cadenas de texto
print("Hola" > "Python")
print("Hola" < "Python")
print("aaaa" >= "abaa")  # Ordenación alfabética por ASCII (no cuenta caracteres) a no es mayor que b --> Por eso sale false
print(len("aaaa") >= len("abaa"))  # Cuenta caracteres
print("Hola" <= "Python")
print("Hola" == "Hola")
print("Hola" != "Python")

### Operadores Lógicos ###

# Basada en el Álgebra de Boole https://es.wikipedia.org/wiki/%C3%81lgebra_de_Boole
print(3 > 4 and "Hola" > "Python") #&&
print(3 > 4 or "Hola" > "Python")  #||
print(3 < 4 and "Hola" < "Python")
print(3 < 4 or "Hola" > "Python")
print(3 < 4 or ("Hola" > "Python" and 4 == 4)) #Hace primero lo del parentesis (como en mates)
print(not (3 > 4)) # !=

#Logica booleana

"""
and
false y false = false
true y false = false
true y true = true

or
false o false = false
true o true = true
true o false = true

not
no false = true
no true = false
"""