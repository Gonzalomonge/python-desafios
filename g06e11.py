"""
Cargar los nombres y fechas de nacimiento de varias personas, luego recorrer y mostrar los nombres de los mayores de edad.
"""
##Cargar los nombres y fechas de nacimiento de varias personas.
añoactual = int(2026)
mesactual = int (4)
diaactual = int(26)
nombres = {'gonzalo': '2/2/2007',
    'rocio':'26/1/2006',
    'fran':'5/5/2000'
    }
#Reocorrer y mostrar los mayores de edad=
for nombre,fechas in nombres.items():
    corte = fechas.split("/")
    dia = int(corte[0])
    mes = int(corte[1])
    año = int(corte[2])
    edad = añoactual - año
    if edad > 18:
        print(nombre)

    elif edad == 18:
        if mes < mesactual or (mes == mesactual and dia <= diaactual):
            print(nombre)
