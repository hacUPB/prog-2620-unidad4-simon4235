peliculas_favoritas = []

while True:
    print("1. Agregar película\n2. Eliminar película\n3. Eliminar una película en específico")
    opcion = int(input("Seleccione la opción del 1 al 3: "))
    if opcion == 1:
        posicion = int(input("Ingrese la posición en la que quiere agregar la película: ")) - 1
        pelicula = input("Ingrese la peícula que desea agregar: ")
        peliculas_favoritas.insert(posicion, pelicula)

    elif opcion == 2:
        pelicula = input("Ingrese la peícula que desea eliminar: ")
        peliculas_favoritas.remove(pelicula)
    
    else:
        posicion = int(input("Ingrese la posición en la que quiere eliminar la película: ")) - 1
        peliculas_favoritas.pop([posicion])

    print(peliculas_favoritas)