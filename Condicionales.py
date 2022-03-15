num1 = 15
num2 = 20
if num1 != num2:
	print('Se ejecuta el if.')

num1 = 1450
num2 = 60
if num1 > num2:
	print('Se ejecuta el if.')

num1 = 60
num2 = 60
if num1 != num2:
	print('Se ejecuta el if.')

color = "rojo"
if color != "rojo":
    print("El color no es rojo.")
else:
    print("El color es rojo.")

edad = int(input('¿Cuál es tu edad?\n'))
if edad <= 0:
	print('Nadie puede tener esa edad.')
elif edad <= 1 and edad < 18:
	print('Eres menor de edad.')
elif edad == 18 and edad <= 45:
	print('Eres mayor de edad.')
elif edad <= 100:
	print('Eres mayor de edad.')
elif edad > 100 and edad <= 120:
	print('Eres muy mayor.')
else:
	print('Edad no válida.')

colores = input('Introduce un color:\n')
tupla_colores = ('rojo', 'azul', 'verde', 'amarillo')
if colores in tupla_colores[0]:
	print('El color rojo está admitido')
elif colores in tupla_colores[1]:
	print('El color azul está admitido')
elif colores in tupla_colores[2]:
	print('El color verde está admitido')
elif colores in tupla_colores[3]:
	print('El color amarillo está admitido')
else:
	print('Color no admitido')