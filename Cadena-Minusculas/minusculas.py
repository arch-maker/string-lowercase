# Conversor de cadenas en minusculas.

while True:
    # Introducimos una cadena de texto que contengan mayusculas.
    cadena = input("Introduce una cadena de texto con mayusculas: ")

    # Imprimimos la cadena en minusculas haciendo uso del metodo .lower()
    print(cadena.lower())

    # Se añadio un control para volver a usar el conversor.
    opcion = input("¿Desea volver a usar la aplicacion? (yes/no): ")

    # El programa termina con un 'break' en caso contrario, controlando las mayusculas introducidas con metodo .lower()
    if opcion.lower() != "y" and opcion.lower() != "yes":

        break