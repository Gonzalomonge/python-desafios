"""
Dado el siguiente diccionario: inventario = {"camisetas": 10, "pantalones": 5, "zapatos": 3, "camisas": 8}, elimina el artículo zapatos y duplica las cantidades de todos los otros artículos. Muestra el inventario actualizado.
"""
###Del diccionario dado, eliminar el articulo zapatos 
## luego duplicar las cantidades de los otros articulos
# mostrar el inventaario actualizado
inventario = {"camisetas": 10, "pantalones": 5, "zapatos": 3, "camisas": 8}
del inventario['zapatos']
inventario['camisetas']=10 * 2 
inventario['pantalones']=5 * 2
inventario['camisas']= 8 * 2
print(inventario)

