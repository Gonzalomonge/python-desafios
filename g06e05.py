"""
Dado el diccionario persona creado en el ejercicio número 1, sumale 10 a la edad y agrega una nueva clave "profesión y años de experiencia" con los valores Ingeniero para profesión y 13 para los años de experiencia. Muestra el diccionario actualizado.
"""
# Dado un diccionario 
#sumarle +10 a la edad [x]
# agregarle una nuevla clave llamada "profesion y años de experiencia" []
## clave profesion /valor:ingeniero _ clave :años de experiencia / valor:13
persona = {'nombre':'Gonzalo','edad': 19,'ciudad':'Rio cuarto'}
persona['edad']=19+10
persona['profesion y años de experiencia']={'profesion': 'ingeniero',
'años de experiencia:':13}
print(persona)
