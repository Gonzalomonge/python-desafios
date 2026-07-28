#Hacer una función que dibuje una raya con un caracter y una longitud dada.

def raya(cant, caract):
    for x in range(cant): 
        print(caract, end="")
    print()
raya(29, '-')
