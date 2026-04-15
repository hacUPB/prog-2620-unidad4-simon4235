opcion = 0
flota = {}

def agregar_aeronave():
    matricula = input("Ingrese la matrícula de la aeronave: ")
    modelo = input("Ingrese el modelo de la aeronave: ")
    horas_vuelo = int(input("Ingrese las horas de vuelo de la aeronave: "))
    componentes = {}
    flota[matricula] = {"modelo": modelo, "horas_vuelo": horas_vuelo, "componentes": componentes}
    
    while True:
        print("1. Agregar componente\n2. Salir")
        opcion = int(input("Ingrese el número de la opción que desea seleccionar: "))
        if opcion == 1:
            componente = input("Ingrese el nombre del componente: ")
            horas_uso = int(input("Ingrese las horas de uso del componente: "))
            limite = int(input("Ingrese el limite de horas de la pieza: "))
            componentes[componente] = {"horas_uso": horas_uso, "limite": limite}
            print(f"componente {componente} agregado.")
            print(componentes[componente])
        else:
            print(f"Aeronave {matricula} agregada a la flota.")
            print(flota[matricula])
            break

def eliminar_aeronave():
    matricula = input("Ingrese la matrícula de la aeronave a eliminar: ")
    if matricula in flota:
        del flota[matricula]
        print(f"Aeronave {matricula} eliminada de la flota.")
    else:
        print("Aeronave no encontrada.")

def modificar_aeronave():
    matricula = input("Ingrese la matrícula de la aeronave a modificar: ")
    if matricula in flota:
        modelo = input("Ingrese el nuevo modelo de la aeronave: ")
        flota[matricula]["modelo"] = modelo
        horas_vuelo = int(input("Ingrese las nuevas horas de vuelo de la aeronave: "))
        flota[matricula]["horas_vuelo"] = horas_vuelo

        while True:
            print("1. Agregar componente\n2. Modificar componente\n3. Eliminar componente\n4. Salir")
            opcion = int(input("Ingrese el número de la opción que desea seleccionar: "))
            if opcion == 1:
                componente = input("Ingrese el nombre del componente: ")
                horas_uso = int(input("Ingrese las horas de uso del componente: "))
                limite = int(input("Ingrese el limite de horas de la pieza: "))
                flota[matricula]["componentes"][componente] = {"horas_uso": horas_uso, "limite": limite}
                print(f"componente {componente} agregado.")
                print(flota[matricula]["componentes"][componente])
            elif opcion == 2:
                componente = input("Ingrese el nombre del componente a modificar: ")
                horas_uso = int(input("Ingrese las horas de uso del componente: "))
                limite = int(input("Ingrese el limite de horas de la pieza: "))
                flota[matricula]["componentes"][componente] = {"horas_uso": horas_uso, "limite": limite}
                print(f"componente {componente} modificado.")
                print(flota[matricula]["componentes"][componente])
            elif opcion == 3:
                componente = input("Ingrese el nombre del componente a eliminar: ")
                del flota[matricula]["componentes"][componente]
                print(f"componente {componente} eliminado.")
            else:
                print(f"Aeronave {matricula} modificada.")
                break
    else:
        print("Aeronave no encontrada.")

def consultar_mantenimiento():
    for matricula, datos in flota.items():
        componentes = datos["componentes"]
        if not componentes:
            print(f"Aeronave {matricula} no tiene componentes registrados.")
            continue
        for nombre, datos_componentes in componentes.items():
            if datos_componentes["horas_uso"] > datos_componentes["limite"]:
                print(f"Aeronave {matricula}: El componente {nombre} requiere mantenimiento.")
            else:
                restante = datos_componentes["limite"] - datos_componentes["horas_uso"]
                print(f"Aeronave {matricula}: El componente {nombre} le restan {restante} horas de uso.")

while True:
    print("1. Agregar aeronave\n2. Eliminar aeronave\n3. Modificar aeronave\n4. Consultar mantenimiento\n5. Imprimir flota\n6. Salir")
    opcion = int(input("Ingrese el número de la opción que desea seleccionar: "))
    if opcion == 1:
        agregar_aeronave()
    elif opcion == 2:
        eliminar_aeronave()
    elif opcion == 3:
        modificar_aeronave()
    elif opcion == 4:
        consultar_mantenimiento()
    elif opcion == 5:
        print(flota)
    else:
        break