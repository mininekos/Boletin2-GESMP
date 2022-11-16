
def max_in_list(lista, cont=0, max=0):

    for num in lista:
        if cont == 0:
            max = num
        elif num > max:
            max = num
    return max

print(max_in_list([0,2,0,25,47,214]))
