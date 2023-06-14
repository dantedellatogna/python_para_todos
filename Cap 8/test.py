t = ['d', 'c', 'e', 'b', 'a']
# t = t.sort()
print(t)
del t[2]
t.remove('d')
print(t)

cadena = 'hola1como1estas1amigo1mio'
cadena = cadena.split('1')
print(cadena)
lista = ['Me', 'Llamo', 'Juan', 'Pablo']
delimitador = ' '
print(delimitador.join(lista))
t = [1, 2, 3, 4]
x = 5
t = t + x
print(t)