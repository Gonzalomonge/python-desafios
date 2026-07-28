"""Almacenar en dos  listas paralelas, nombres y sexos de 8 personas. Al finalizar, recorrerlas y mostrar los nombres de las mujeres. 
Dos funciones: carga y mostrar_mujeres"""
## crear 2 listas de nombres y sexoa
def names():
    name = ['gonzalo','rocio', 'marta','albertito']
    sex = ['m','f','f','m']
    return(name,sex)

def recorrido(name,sex):
    mujeres = ''   
    for i in range(len(name)):
        if sex[i] == 'f':
            print(name[i])
name,sex = names()
recorrido(name,sex)

