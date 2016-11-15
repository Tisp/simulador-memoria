''' Transforma uma lista em uma lista de pares de tuplas '''
def listPairs(l):
    ''' verifica se a lista tem numeros pares
    de elementos '''
    if len(l) % 2 != 0:
        return None

    arr = []
    i = 0

    while i < len(l) - 1:
        arr.append((l[i], l[i+1]))
        i += 2
    
    return arr
        
        
