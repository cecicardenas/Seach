lista=[4,21,36,14,62,91,8,22,7,82,77,19]
print(lista)
objetivo=910
lista.sort()

def busquedaBinaria(lista,objetivo):
    primer=0
    ultimo=len(lista)-1
    encontrado=False

    while primer<=ultimo:
        medio=int((primer+ultimo)/2)
        if objetivo==lista[medio]:
            encontrado=True
            break
        elif objetivo<lista[medio]:
            ultimo=medio-1
        else:
            primer=medio+1
    return encontrado
    
print(busquedaBinaria(lista, objetivo))
