'''
Ejercicio 1: Escribe un programa que lea repetidamente números hasta
que el usuario introduzca “fin”. Una vez se haya introducido “fin”,
muestra por pantalla el total, la cantidad de números y la media de
esos números. Si el usuario introduce cualquier otra cosa que no sea un
número, detecta su fallo usando try y except, muestra un mensaje de
error y pasa al número siguiente.
'''

n = ''
nfloat = 0
total = 0
cantidad = 0

while n != None and n!= 'fin':
    try:
        n = input('Introduzca un número: ')
        nfloat = float(n)
        total += nfloat
        cantidad += 1
    except:
        print('Error. Elemento no valido.')

print(f'Total: {total}')
print(f'Cantidad: {cantidad}')
print(f'Media: {total/cantidad}')
