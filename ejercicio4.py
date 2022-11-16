
def contarMayusculas(cadena, mayus=0):
    for cad in cadena:
        if cad.isupper():
            mayus += 1
    print(mayus)


print("Introduzca una cadena: ")
cadena = input()

contarMayusculas(cadena)