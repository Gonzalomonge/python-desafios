 #Buscar una palabra y reemplazarla por otra todas las veces que aparezca. Ej.: ‘peras’ en lugar de ‘manzanas’ quedaría 'Quiero comer peras, solamente peras.'  
# sin comas ni puntos.

"""
texto = "Quiero comer manzanas , solamente manzanas."
textofinal = texto.split(' ')
print(textofinal)
palabra_buscada = input('Ingrese la palabra buscada:')
palabra_abuscar = input('Palabra a reemplazar:')
for palabra in textofinal:
    if palabra == palabra_buscada:
        palabra = palabra_abuscar
if palabra in textofinal:
    palabra = palabra_buscada
    print(palabra_buscada)
"""
texto = "Quiero comer manzanas solamente manzanas"

palabras = texto.split()

for i in range(len(palabras)):
    if palabras[i] == "manzanas":
        palabras[i] = 'Bananas'

texto = " ".join(palabras)

print(texto)


































