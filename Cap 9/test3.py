fname = 'python_para_todos\Cap 9\words_romeo.txt'

try:
    fhand = open(fname)
except:
    print('No se ha encontrado el archivo.')
    exit()

counts = dict()

for linea in fhand:
    palabras = linea.split()
    for palabra in palabras:
        counts[palabra] = counts.get(palabra, 0) + 1

print(counts)
