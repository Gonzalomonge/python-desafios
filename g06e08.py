"""
Dado el siguiente diccionario: notas = {"Juan": 85, "Ana": 92, "Luis": 78, "María": 95}, crea una lista con los nombres de los estudiantes cuyas notas son mayores o iguales a 90.
"""
#dado un diccionario de alumnos y notas
# crear otros con los nombres de los alumnos cuyas notas sean >= a 90
notas = {"Juan": 85, "Ana": 92, "Luis": 78, "María": 95}
aprobados = []
for nombre,nota in notas.items():
    if nota >= 90:
        aprobados.append(nombre)
print(f'Los alumnis cuyas notas son mayores a 90 son {aprobados}')
