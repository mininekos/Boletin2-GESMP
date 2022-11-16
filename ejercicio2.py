def mas_larga(lista,max=""):

    for cadena in lista:
        if len(cadena) > len(max):
            max = cadena
    return max


print(mas_larga(["1", "12", "123"]))