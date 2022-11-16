
def superposicion(lista1,lista2):
    for i in lista1:
        for j in lista2:
            if i == j:
                return True
    return False


print(superposicion([1, 2, 3, 4], [0, 0, 0, 0]))
