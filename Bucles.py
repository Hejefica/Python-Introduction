x = 0
while x <= 15:
	print(x)
	x += 5

x = 0
while x >= -100:
	print(x)
	x -= 20

x = 10
while x >= 0:
	print('El valor de x es: ', x)
	x -= 1

x = 0
while x <= 30:
	x += 1
	if x == 4 or x == 6 or x == 10:
		print('Se saltó el valor ', x, ' de x')
		continue
	if x == 15:
		print('Se rompió la ejecución del bucle cuando x valía: ', x)
		break
	print(x)

colores = ('rojo', 'azul', 'verde', 'amarillo')
for x in colores:
	print('El color es: ' + x + '.')

for x in range(7, 700, 100):
	print(x)

