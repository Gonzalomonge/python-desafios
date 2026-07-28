#Contar la cantidad de letras (mayúsculas, minúsculas, acentuadas, eñes). El resultado es el total general.
def cont(frase):
    contador = 0
    for caracter in frase:
        contador += 1
    return(contador)
print(cont(" Quiero comer manzanas,solamente manzanas."))
