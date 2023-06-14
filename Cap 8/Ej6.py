entrada = ''
numeros = []
# ciclo que termine cuando el usuario ingresa 'hecho'
while entrada != 'hecho':
    entrada = input('Introduzca un número: ')
    #almacenar entrada de usuario (numeros) en lista
    try:
        entrada_f = float(entrada)
        numeros.append(entrada_f)
    except:
        if entrada != 'hecho':
            print('Por favor, introduzca un número.')
        continue
# usar max() y min() en la lista resultante
print(f'Máximo: {max(numeros)}')
print(f'Mínimo: {min(numeros)}')