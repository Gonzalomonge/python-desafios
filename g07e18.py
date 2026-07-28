#Hacer una función que determine si una cadena de texto contiene todas las vocales.
def vocales(cadena):
    print(f'La  cadena de texto es: {cadena}')
    for vocal in 'aeiou':
        if vocal in cadena:
            print(f'{vocal} Esta en la cadena')
        else:
            print(f'{vocal} No esta')
vocales('hola soy gonzalo')

