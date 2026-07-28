#Ingresar la lluvia caída en milímetros para cada día de la semana. Mostrar al final el total de lluvia caída y el nombre del día que más llovió.
week = ['lunes','martes','miercoles','jueves','viernes']
def rain():
    suma = 0
    max_lluvia = 0
    diamax = ''
    for day in week:
        lluv = int(input(f'el dia {day} llovio:'))
        suma = suma + lluv
        #Dia maximo
        if lluv > max_lluvia :
            max_lluvia = lluv
            diamax = day
    print(f'El total de lluvia es de {suma} mm')
    print(f'El dia que mas llovio fue el {diamax}')    
rain()

