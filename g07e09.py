# Dada una lista cargada con números enteros, obtener el promedio de ellos. Mostrar por pantalla dicho promedio y los números ingresados que sean mayores que él. Dos funciones: promedio y mayor_que.
#1era funcion: lista con numeros entero, obtener el promedio.
lista = [1,2,3,4,5,6]
def prom(lista):
    cant = len(lista)
    suma = 0
    for num in lista:
        suma += num
    promedio = suma / cant
    return(promedio)
print(f'El promedio de los numeros de la lista es:{prom(lista)}')
print(f'los numerso mayores al promedio son:')
#2da funcion: numero ingresados mayores que el promedio : 3.5
def mayor():
    for i in lista:
        if i > prom(lista):           
            print(i)

mayor()
