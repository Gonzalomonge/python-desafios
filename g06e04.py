"""
Crea un diccionario sin carga (con una iteración automática) donde las claves sean números del 1 al 5 y los valores sean sus respectivos cuadrados. Luego, muestra el diccionario.
"""
numeros = { }

for i in range(1,6):
    
    numeros[i]= i**2
print(numeros)
    
