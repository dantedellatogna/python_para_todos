# Abrir archivo mbox-short.txt
archivo = open('mbox-short.txt')
correos =[]
# Leer archivo linea por linea e imprimir y contar las que empiecen con From
# No incluir 'From:'
for linea in archivo:
    palabras_linea = linea.split()
    try:
        if palabras_linea[0] == 'From':
            correos.append(palabras_linea[1])
    except:
        continue
# Solo imprimir segunda cadena

for correo in correos:
    print(correo)

print(f'Hay {len(correos)} en el archivo con la palabra From al inicio.')