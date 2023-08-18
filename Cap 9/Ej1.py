import random

archivo = open('.\Cap 9\words.txt')
palabras = dict()

for linea in archivo:
    for palabra in linea.split():
        palabras[palabra] = random.randint(0, 100)

print(palabras)
buscar_p = 'know'
if buscar_p in palabras:
    print(f'La palabra "{buscar_p}" está en el diccionario')
else:
    print(f'La palabra "{buscar_p} NO está en el diccionario')