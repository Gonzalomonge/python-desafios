# Y el más bonito! Hacer una función que reciba una cadena de texto,por ejemplo: 
def recu(texto,texto1):
    esi = '╔'
    esd = '╗'  
    floor = '═' 	
    wall = '║' 
    eii = '╚'
    eid = '╝'
    print(f'{esi}{floor * len(texto)}{esd}')
    print(f'{wall}{texto}{wall}')
    print(f'{eii}{floor * len(texto)}{eid}')
    
    print(f'{esi}{floor * len(texto1)}{esd}')
    print(f'{wall}{texto1}{wall}')
    print(f'{eii}{floor * len(texto1)}{eid}')
recu('Gonzalo', 'HOLA COMO ESTAS')
