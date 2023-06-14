def recortar(lista):
    lista.pop(0)
    lista.pop()
    return None

def medio(lista):
    lista = lista[1:-1]
    return lista

if __name__ == '__main__':
    lista1 = [1, 2, 3, 4, 5]
    lista2 = ['a', 'b', 'c', 'd', 'e']

    recortar(lista1)
    print(lista1)

    lista2_modificada = medio(lista2)
    print(lista2_modificada)
    print(lista2_modificada is lista2)

