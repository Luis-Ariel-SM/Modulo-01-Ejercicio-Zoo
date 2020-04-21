import screen_modulo

# Funcion para calcular los precios segun rango de edad
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

# Funcion para valida la edad. Que el numero sera entero y positivo
def valida_edad (edad):
    try:
        n = int(edad) # Que sea entero
        if n >= 0: # Y que sea positivo
            return True
        else:
            return False
    except:
        return False

# Funcion para la entrada de datos, se llama a la funcion de validacion en la misma, se itera hasta lograr el dato correcto.
def pedir_edad ():
    screen_modulo.locate(1,1)
    edad = input ("¿Que edad tienes? ")
    while valida_edad (edad) == False:
        print ("Edad incorrecta, vuelvela a introducir")
        screen_modulo.locate(1,1)
        edad = input ("¿Que edad tienes? ")
        
    return int(edad) # Interesante como en el mismo return se puede transformar la cadena a enteros, tomar nota

screen_modulo.clear()
# Inicio del programa, entrada de datos invocando a la funcion y metiendo el resultado en la variable
edad = pedir_edad ()
    
precio_total = 0

while edad != 0:
    
    precio_entrada = calcular_precio_entrada (edad)
    print ("Precio entrada: {}".format(precio_entrada))
    precio_total += precio_entrada
    
    edad = pedir_edad () 
    
print ("total: {}".format(precio_total))