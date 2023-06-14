import os
fpath = 'texto_prueba.txt'
if not os.path.exists(fpath):
    print('File does not exist.')
else:
    manejador = open('texto_prueba.txt')
    contador = 0

    for linea in manejador:
        palabras = linea.split()
        #print('Depuración:', palabras)
        if len(palabras) == 0:
            continue
        if len(palabras) < 3 or palabras[0] != 'From':
            continue
        print(palabras[2])