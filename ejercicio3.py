
def filtrar_palabras(lista,numCaracter):
    for cadena in lista:
        if len(cadena) > numCaracter-1:
            print(cadena)


print(filtrar_palabras(["1", "12", "123"],2))