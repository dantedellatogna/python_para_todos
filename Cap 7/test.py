manejador_archivo = open('Python para todos\Cap 7\pepe.txt')
print(manejador_archivo)
contador = 0
for i in manejador_archivo:
    contador = contador + 1
print('contador de lineas: ', contador)

manejador_archivo = open('Python para todos\Cap 7\pepe.txt')
imp = manejador_archivo.read()
print(len(imp))
print(imp)

print('aaa')
manejador_archivo = open('Python para todos\Cap 7\pepe.txt')
forimp = manejador_archivo.read()
forimplist = forimp.split('\n')
contadorfor = 0
for i in forimplist:
    print(i)
    contadorfor += 1
print('Contador for: ', contadorfor)