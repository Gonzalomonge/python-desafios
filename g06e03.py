"""
rea un diccionario con los nombres de tus amigos como claves y sus alturas como valores. Luego, itera sobre el diccionario e imprime cada nombre seguido de su altura y un cartel al lado que diga "(es alto)" cuando supere el metro ochenta. 
Salida ejemplo:
Pipo mide 1.65
Pocho mide 1.90 (es alto)
Laura mide 1.55
"""
###crear un diccionario con los nombres de mis amigos 
## nombres como claves , alturas como valores
#ierar sobre le diccionario
# crear una condicion sii su altura supera el metro ochentaç
amigos = {'gonzalo': 179 , 'fran': 181 , 'tiago' : 171}


for i in amigos:
    if amigos[i] > 180:
        print(f'{i}, mide {amigos[i]}, (es alto)')
    else:
        print( i ,'mide', amigos[i])
    
    
     
