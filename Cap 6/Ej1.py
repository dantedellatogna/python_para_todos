'''
Ejercicio 1: Escribe un bucle while que comience con el último carácter
en la cadena y haga un recorrido hacia atrás hasta el primer carácter
en la cadena, imprimiendo cada letra en una línea independiente.
'''

cadena = "supermercado"

letra = len(cadena) - 1
while letra >= 0:
    print(cadena[letra])
    letra -= 1

print('2')
print(cadena[:])
print('3')