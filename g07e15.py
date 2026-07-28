#Escribe una función que determine si dos listas tienen algún elemento en común.
lista1 =['hola','chau','adios','nosvemos']
lista2 = ['gonzalo','alberto','adios','chau']
def foo():
    repetidos = []
    for i in lista1:
        for x in lista2:
            if i == x:
                repetidos.append(i)
    return repetidos 
print(f'Los elementos repetidos en las listas son:{foo()}')    
