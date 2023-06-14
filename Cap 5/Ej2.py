'''
Ejercicio 2: Escribe otro programa que pida una lista de números como
la anterior y al final muestre por pantalla el máximo y mínimo de los
números, en vez de la media.
'''

n = ''
nfloat = None
maximo = None
minimo = None

while n == None or n!= 'fin':
    try:
        n = input('Introduzca un número: ')
        nfloat = float(n)
        if maximo == None and minimo == None:
            maximo = nfloat
            minimo = nfloat

        if nfloat > maximo:
            maximo = nfloat

        if nfloat < minimo:
            minimo = nfloat

    except:
        print('Error. Elemento no valido.')

print(f'Valor máximo: {maximo}')
print(f'Valor mínimo: {minimo}')
