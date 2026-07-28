"""
Primer bucle: Almacenar nombres y sexos de personas hasta que el usuario diga que no hay más. 
Segundo bucle: Recorrer y guardar los nombres de las mujeres en una lista. 
Tercer bucle: Mostrar los elementos de la lista resultante.
"""
## Almacenar nombres y sexos de personas en una lista
## recorrr y guardar los nombres de las mujeres
# Mostrar la lista resultante
nombres = []
sexos = []
mujeres = []
haymas = 'si'
while haymas == 'si':
    nombre = input('ingrese un nombre:')
    nombres.append(nombre)
    sexo = input('ingrese sexo:')
    sexos.append(sexo)
    if sexo == 'f':
        mujeres.append(nombre)         
    haymas = input('hay mas personas?(si/no):')
print(f'Mujeres en la lista:{mujeres}')
