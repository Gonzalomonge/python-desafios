#Crea una función que calcule la suma de los dígitos de un número entero.
def sumar(numero):
    suma = 0
    for digito in str(numero):    #Str para poder recorrerlo, sino no me deja recorrer el numero.
        suma += int(digito)
    return suma
print(f'La suma de los digitos es: {sumar(1010)}')

