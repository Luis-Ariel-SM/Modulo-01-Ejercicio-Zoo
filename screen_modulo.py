def clear ():
    print("\033[2J")

def locate (linea, columna):
    print("\033[{};{}H".format(linea, columna), end = "")

clear()
locate (5,5)