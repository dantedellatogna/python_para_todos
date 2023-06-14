try:
    narchivo = input('Introduzca el nombre del archivo a abrir: ')
    archivo = open(narchivo)
    total = 0
    contador = 0
    for linea in archivo:
        if linea.startswith('X-DSPAM-Confidence:'):
            space_index = linea.index(' ')
            valor = float(linea[space_index + 1:])
            total += valor
            contador += 1
            print(valor)

    promedio = total / contador
    print('Promedio spam confidence: ', promedio)
except:
    if narchivo == 'na na boo boo':
        print('NA NA BOO BOO PARA TI - Te he atrapado!')
    else:
        print('El archivo no puede ser abierto: ', narchivo)