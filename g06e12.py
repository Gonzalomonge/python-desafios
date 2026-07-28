"""
Crea una lista a mano con al menos 3 elementos, el primero de ellos debe ser el diccionario persona que obtuvimos como salida en el ejercicio número 5. Los siguientes elementos de la lista deben ser diccionarios similares (tipo registro). Luego muestra los nombres de todas las ciudades y el promedio de los años de experiencia de los profesionales.
"""
personas =[ 
{'nombre':'Gonzalo','edad': 19,'ciudad':'Rio cuarto','experiencia':3},
{'nombre':'rocio','edad': 20,'ciudad':'san basilio','experiencia':1},
{'nombre':'alberto','edad':50,'ciudad':'cordoba','experiencia':15}]
promedio = 0
           ## Mostrar los nombres de todas las ciudades
suma_experiencia = 0
for persona in personas:
    print('ciudades:',persona['ciudad'])
          ##el promedio de los años de experiencia de los profesionales
    suma_experiencia += persona['experiencia']
print('Promedio:',suma_experiencia / 3)
