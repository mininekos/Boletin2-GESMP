
def procedimiento(lista,cadena=""):
    for num in lista:
        cadena = ""
        for a in range(num):
            cadena += "*"
        print(num, ": ", cadena)


procedimiento([4, 9, 7])