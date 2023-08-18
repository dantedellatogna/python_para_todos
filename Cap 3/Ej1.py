horas = float(input('Introduzca las Horas: '))
tarifa = float(input('Introduzca la Tarifa por hora: '))
salario = horas * tarifa
if horas > 40:
    salario *= 1.5

print(f'Salario: {salario}')
