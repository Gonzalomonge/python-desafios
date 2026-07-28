#Ingresar nombres, luego buscar un nombre y de encontrarlo decir en qué posición está. 
def names():
    nombres = []
    for name in range(4):
        name = input('ingrese un nombre:')
        nombres.append(name)
    name_bus = input('que nombre esta buscando:')
    
    for i in range(len(nombres)):    
        if nombres[i] == name_bus:
            return i
print(f'El nombre buscado esta en la posicion {names()}')

        
