"""c Cuántas veces se repite una letra cualquiera. Parámetros: letra, cadena.
"""

def texto(letra, cadena):
    contador = 0  
    for caracter in cadena:
        if letra == caracter:
            contador += 1
    return(contador)
print(texto('a','Quiero comer manzanas, solamente manzanas.'))
