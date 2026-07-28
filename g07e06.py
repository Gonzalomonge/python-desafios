# Definir una lista con 10 letras. Contar las vocales y mostrar el total.
def vocales():
    lista =['a','b','e','o','c','d','f','g','u']
    contador = 0
    for n in lista:
        if n in ('a','e','i','o','u'):
            contador += 1
    return(contador)
print(f'el numero de vocales en la lista es de {vocales()}')   # Colocarlo dentro de una string.
