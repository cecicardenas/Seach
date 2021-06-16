lista=[4,21,36,14,62,91,8,22,7,82,77,19]
objetivo=620
i=0
resultado=""
valor=0
pos=0
for num in lista:
    if num==objetivo:
        valor=num
        pos=i
        resultado="El numero ", valor, " se encuentra en la pocision ", pos
        break;
    else:
        resultado="El numero no se encuentra en la lista"
    i=i+1
print(resultado)
