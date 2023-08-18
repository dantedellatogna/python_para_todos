palabra = 'brontosaurio'

letras = dict()

for i in palabra:
    #if i not in letras:
    #    letras[i] = 1
    #else:
    #    letras[i] += 1
    letras[i] = letras.get(i, 0) + 1
print(letras)