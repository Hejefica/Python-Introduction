numeros = ["tres", "dos", "cinco", "cuatro", "uno"]

colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']
#naranja, amarillo, lila, blanco, rojo
print(colores[-1],colores[-7],colores[-5],colores[-2],colores[-10])

del colores[1]
del colores[3]
del colores[4]
del colores[-3]
print(colores)

colores.remove('amarillo')
colores.remove('rojo')
print(colores)

colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']
color1 = colores.pop(1)
color2 = colores.pop(7)
colores_guardados = [color1, color2]
print(colores)
print(colores_guardados)

colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']
colores.append('fuxia')
colores.append('celeste')
print(colores)

colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']
colores.insert(-4, 'magenta')
colores.insert(-1, 'turquesa')
print(colores)

colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón','lila', 'negro', 'rosa', 'blanco', 'naranja']
colores.sort(reverse=True)
print(colores)

colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']
colores_tupla = tuple(colores)
print(type(colores_tupla))