#Averiguar qué cantidad de letras tiene la palabra más larga.  Para ello, primero cargar cada palabra en una lista y luego obtener la solicitada. Usar dos funciones.
def texto(frase):   ## Frase separada en listas
    lista = frase.split(' ')
    print(lista)
texto("Quiero comer manzanas, solamente manzanas.")

def longitud(lista):
    caracteres = ''
    for caracter in lista:              
        if len(caracteres) < len(caracter):
            caracteres = palabra
            return(caracteres)
        
longitud()           
        
