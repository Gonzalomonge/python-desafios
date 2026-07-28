
#Escribe una función que encuentre el número que más se repite en una lista.
numeros =[]
def foo(numeros):

    dicc = {}
    for num in numeros: 
        if num in list(dicc.keys()):
            dicc[num] += 1
        else:
            dicc[num] = 1
        numero_mayor = 0
        cantidad_mayor = 0
    for num,cantidad in dicc.items():
        if cantidad > cantidad_mayor:   
            cantidad_mayor = cantidad
            numero_mayor = num
            print(f'el numero mayor es {numero_mayor} y su cantidad es {cantidad_mayor}')
foo('1,2,1,1')
    
    

