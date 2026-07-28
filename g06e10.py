"""
Ingresar la lluvia caída en milímetros para cada día de la semana. Mostrar al final el total de lluvia caída y el nombre del día que más llovió (sin repetir cantidades). 
"""
semana = ['lunes','martes','miercoles','jueves','viernes']
lluvia = { }
for dia in semana:
    dias = int(input(f'Ingresa la cantidad que llovio el {dia}:'))
    lluvia[dia]=dias
total = 0
for valor in lluvia.values():
    total = valor + total
print(f'La cantidad de lluvia caida es: {total} milimetros')     
#Dia que mas llovia
maximo = int (0)
diamayor = 0
for dias,valor in lluvia.items():
    if valor > maximo:
        maximo = valor       
        diamayor = dias
print(f'El dia que mas llovio fue el:{diamayor}')
