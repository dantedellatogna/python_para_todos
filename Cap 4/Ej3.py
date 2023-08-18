def calculo_salario(horas, tarifa):
    try:
        salario = horas * tarifa
        if horas > 40:
            salario *= 1.5
        print(f'Salario: {salario}')
    except:
        print('Error. Por favor, introduzca un valor numérico.')


horas = float(input('Introduzca las Horas: '))
tarifa = float(input('Introduzca la Tarifa por hora: '))

calculo_salario(horas, tarifa)
