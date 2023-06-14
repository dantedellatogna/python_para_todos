'''
El siguiente programa cuenta el número de veces que la letra “a” aparece en una
cadena:

palabra = 'banana'
contador = 0
for letra in palabra:
    if letra == 'a':
        contador = contador + 1
print(contador)

Este programa demuestra otro patrón de computación llamado contador. La variable contador es inicializada a 0 y después se incrementa cada vez que una “a” es
encontrada. Cuando el bucle termina, contador contiene el resultado: el número
total de a’s.
Ejercicio 3: Encapsula este código en una función llamada cuenta, y
hazla genérica de tal modo que pueda aceptar una cadena y una letra
como argumentos.
'''

def cuenta(cadena, letra):
    contador = 0
    for i in cadena:
        if i == letra:
            contador = contador + 1
    return contador

cadena = 'colombia'
letra = 'o'

print(cuenta(cadena, letra))