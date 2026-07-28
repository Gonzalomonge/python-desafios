#Implementa una función que determine si una cadena de texto contiene solo caracteres numéricos (es decir, si es un entero).
def fun():
    cadena = '1b234e5678i9'
    for i in cadena:
        if i in '0123456789':
            print(f'{i} = Es un entero')
        else:
            print(f'{i} No es un entero')
fun()     
    
