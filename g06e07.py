"""
Crea un diccionario con varios países y capitales. Pide al usuario que ingrese el nombre de un país y muestra la capital correspondiente si existe en el diccionario. Si no existe, muestra un mensaje indicando que el país no se encuentra en el diccionario.
"""
### Crear un diccionario con varios paises y capitales
## pedir que ingrese un pais y su capital correspondiente
# si no existe mostrar un cartel que diga 'El pais no se encuentra en el diccionario.'
paises = {'argentina': 'buenos aires', 'mexico':'ciudad de mexico', 'uruguay':'montevideo'}
haypaises = 'si'
while haypaises == 'si':
    pais = input('ingrese un pais:')
    if pais in paises:
        print('La capital de el pais es', paises[pais])
    else:
        print('El pais no se encuentra en el diccionario')
    haypaises = input('hay mas paises? (si/no):')

