#Pedir el ingreso de un nombre completo (Juan Pérez) y mostrarlo invertido y con coma (Pérez, Juan).
def names():
    name = input('ingrese su nombre:')
    nickname = input('ingrese su apellido:')

    reverse = nickname +  ',' + name    
    return reverse
print(names())
