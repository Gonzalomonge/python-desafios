#Cargar en listas los nombres y fechas de nacimiento de varias personas, luego recorrerlo y mostrar los nombres de los mayores de edad. Funciones de carga y cálculo de edad.
lista = ['gonzalo','rocio','fran','tito']
lista2 = ["2/2/2007", "26/2/2009", "1/5/2010", "3/9/2000"]
def mayor():
    años = []

    for cortes in lista2:
        fechas = cortes.split('/')
        año = int(fechas[2])
        años.append(año)
    return(años)
def calculo():
    for i in range(len(mayor())):
        edad = 2026 - mayor()[i]
        if edad > 18:
            print(f'{lista[i]},es mayor de edad')
calculo()
