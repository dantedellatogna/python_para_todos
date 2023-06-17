def calcula_calificacion(nota):
    print('''Puntuación Calificación
      >= 0.9    Sobresaliente
      >= 0.8    Notable
      >= 0.7    Bien
      >= 0.6    Suficiente
      < 0.6     Insuficiente''')

    resultado = ''
    if nota >= 0.9 and nota <= 1.0:
        resultado = 'Sobresaliente'
    elif nota >= 0.8 and nota < 0.9:
        resultado = 'Notable'
    elif nota >= 0.7 and nota < 0.8:
        resultado = 'Bien'
    elif nota >= 0.6 and nota < 0.7:
        resultado = 'Suficiente'
    elif nota < 0.6 and nota >= 0:
        resultado = 'Insuficiente'
    else:
        resultado = 'Puntuación incorrecta'

    return resultado


try:
    nota = float(input('Introduzca puntuación: '))
    print(calcula_calificacion(nota))
except:
    print('Puntuación incorrecta')
