def calcular_precio_entrada (edad):
    if edad > 0 and edad <= 2:
        precio = 0
    elif edad >= 3 and edad <= 12:
        precio = 14
    elif edad >= 12 and edad <= 65:
        precio = 23
    else:
        precio = 18
    return precio

def pedir_edad ():
    edad = input ("Que edad tienes? ")
    edad = int (edad)
    return edad

edad = pedir_edad ()
    
precio_total = 0

while edad != 0:
    precio_entrada = calcular_precio_entrada (edad)
    print ("Precio entrada: {}".format(precio_entrada))
    precio_total += precio_entrada
    
    edad = pedir_edad ()
    
print ("total: {}".format(precio_total))