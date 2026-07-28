#Contar la cantidad de palabras
def cont(frase):
    contador = 0
    for caracter in frase:
            if caracter == ',':
                pass
            elif caracter == '.':
                pass
            else: 
                contador += 1 
            
                
    return(contador)
print("La cantidad de palabras sin puntuación son:",(cont(" Quiero comer manzanas,solamente manzanas.")))

