# 1. Imprime por pantalla el texto "¡Hola, este es mi primer ejercicio!"

print("¡Hola, este es mi primer ejercicio!")

# 2. Crea una variable llamada 'nombre' con tu nombre y otra 'edad' con tu edad.
# Imprímelas en una sola línea usando una coma.

nombre = "Antonio"
edad = 19
print("Hola me llamo",nombre, "y tengo", edad, "años")
#print("Hola me llamo" + nombre + "y tengo: " + edad) esto seria en java

# 3. Imprime el resultado de sumar 150 y 350 directamente dentro de un print.

print(150 + 350)

# 4. Declara una variable de tipo String que sea "100" y otra de tipo Int que sea 100.
# Imprime el tipo de dato de cada una usando la función type().

variable_string_4 = "100"
variable_int_4 = 100
print(type(variable_string_4))
print(type(variable_int_4))

# 5. Crea una variable con un número decimal (float) y conviértela a entero (int).
# Imprime el resultado final.

variable_decimal_to_str_5 = 10.5
print(variable_decimal_to_str_5) 
print(type(variable_decimal_to_str_5)) #float

variable_string_5 = str(variable_decimal_to_str_5) #Conversión (casting)
print(variable_string_5)
print(type(variable_string_5))

# 6. Utiliza un solo print para mostrar tu lenguaje de programación favorito 3 veces seguidas.
# (Pista: usa el operador de multiplicación * con el string).

print("Python " * 3)

# 7. Crea una variable booleana que represente si "5 es mayor que 3" e imprímela.

es_mayor = 5 > 3
print(es_mayor)

# 8. Define tres variables: 'ciudad', 'pais' y 'poblacion' (un número).
# Imprímelas usando un f-string para que quede así: "Vivo en Madrid, España, y tiene 3000000 habitantes".

ciudad = "Madrid"
pais = "España"
poblacion = 3000000

#f-string (f"Texto {variable} texto")
mensaje = f"Vivo en {ciudad}, {pais}, y tiene {poblacion} habitantes"

print(mensaje)

# 9. Declara una variable con el valor 10.5. Imprime un mensaje que diga:
# "El valor es de tipo:" seguido del tipo de esa variable.

numero = 10.5
print("El valor es de tipo:", type(numero))

# 10. Crea una variable 'saludo' que sea "Hola" y otra 'nombre' con tu nombre.
# Concatenalas (únelas con +) para formar un saludo completo con un espacio en medio.

saludo = "Hola"
nombre = "Antonio"

resultado = saludo + " " + nombre
print(resultado)