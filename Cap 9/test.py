archivo = open('./Cap 9/words_romeo.txt')
palabras = {}

for i in archivo:
    words = i.split()
    for j in words:
        palabras[j] = palabras.get(j, 0) + 1

print(palabras)
