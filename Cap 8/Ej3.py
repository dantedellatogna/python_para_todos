# Abrir archivo
archivo = open('romeo.txt')
palabras = []
# Leer archivo linea por linea
for linea in archivo:
    ## Dividir linea en una lista de palabras
    palabras_linea = linea.split()

    ## Comprobar si la palabras ya están en la lista
    for palabra in palabras_linea:
        if palabra not in palabras:
            palabras.append(palabra)

# Ordenar lista
palabras.sort()
print(palabras)