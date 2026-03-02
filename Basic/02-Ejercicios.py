# 1. Calcula el resto de dividir 17 entre 5 (operador módulo %) e imprímelo.

print(17 % 5)

# 2. Eleva el número 2 a la potencia de 10 (2 multiplicado por sí mismo 10 veces) e imprime el resultado.

print(2 ** 10)

# 3. Realiza una "división entera" de 25 entre 4. 
# El resultado debe ser 6 (sin decimales). Usa el operador //.

print(25 // 4)

# 4. Crea una variable 'comparacion' que guarde si 10 es diferente de 5. 
# Imprime el resultado (debería ser True).

comparacion = (10 != 5)
print(comparacion)

# 5. [Lógica] Verifica si (10 > 5) Y (3 < 1) al mismo tiempo usando 'and'. 
# Imprime el resultado.

print(10 > 5 and 3 < 1)

# 6. [Lógica] Verifica si (10 > 5) O (3 < 1) usando el operador 'or'.
# Imprime el resultado.

print(10 > 5 or 3 < 1)

# 7. Compara dos cadenas de texto: "¿Es 'Manzana' igual a 'manzana'?" 
# (Recuerda que Python distingue mayúsculas).

print("Manzana" == "manzana")

# 8. Usa el operador 'not' para invertir el resultado de la comparacion (5 == 5).
# Es decir, debe imprimir False aunque 5 sea igual a 5.

print(not (5 ==5))

# 9. Multiplica el string "Python" por el resultado de la operación (10 // 3).
# ¿Cuántas veces aparecerá la palabra?

print("Python " * (10 // 3))

# 10. Compara el largo (len) de la palabra "Hola" con el largo de la palabra "Java".
# ¿Es el largo de "Hola" mayor o igual al de "Java"? Imprime el booleano.

print(len("Hola") >= len("Java"))