
def generar_n_caracteres(num,caracter,cadena=""):

    for a in range(num):
        cadena += caracter
    return cadena


print(generar_n_caracteres(4, "a"))
