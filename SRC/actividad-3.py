vuelo = {
    "aerolinea": "Avianca",
    "vuelo": "AV123",
    "origen": "BOG",
    "destino": "MDE"
}

ciudad_llegada = vuelo["destino"]
print(ciudad_llegada)

vuelo["destino"] = "CLO"
ciudad_llegada = (vuelo["destino"])
print(ciudad_llegada)

vuelo["estado"] = "En el aire"
print(vuelo)

piloto = vuelo.get("piloto", "pilto no asignado")
print(piloto)

del vuelo["vuelo"]
print(vuelo)

# Base de datos de flota
flota = {
    "N123AA": {
        "modelo": "Boeing 787-9",
        "año": 2018,
        "horas_vuelo": 12500,
        "ciclos": 1350,
        "estado": "En servicio",
        "base": "DFW",
        "proxima_revision": "2023-07-15"
    },
    "N456AA": {
        "modelo": "Boeing 777-300ER",
        "año": 2014,
        "horas_vuelo": 26800,
        "ciclos": 2940,
        "estado": "En mantenimiento",
        "base": "MIA",
        "proxima_revision": "2023-03-30"
    }
}

# Añadir nueva aeronave
flota["N789AA"] = {
    "modelo": "Airbus A321neo",
    "año": 2022,
    "horas_vuelo": 1200,
    "ciclos": 420,
    "estado": "En servicio",
    "base": "LAX",
    "proxima_revision": "2024-01-10"
}

# Actualizar datos de mantenimiento
flota["N456AA"]["estado"] = "En servicio"
flota["N456AA"]["horas_vuelo"] += 12  # Después de un vuelo
flota["N456AA"]["ciclos"] += 1

# Mostrar información detallada
for matricula, datos in flota.items():
    print(f"\\nAeronave: {matricula}")
    for clave, valor in datos.items():
        print(f"  {clave}: {valor}")

# Filtrar aeronaves por modelo

placa = input("Ingrese la placa del avión: ")

temp = {}
    
modelo = input("Ingrese el modelo del avión: "),
ano = input("Ingrese el año del avión: "),
horas_vuelo = input("Ingrese las horas de vuelo del avión: "),
ciclos = input("Ingrese el numero de ciclos del avión: ")
estado = input("Ingrese el servicio del avión: ")
base = input("Ingrese la base del avión: ")
proxima_revision = input("Ingrese la fecha de la proxima revisión del avion: ")

temp["modelo"] = modelo
temp["ano"] = ano
temp["horas_vuelo"] = horas_vuelo
temp["ciclos"] = ciclos
temp["estado"] = estado
temp["base"] = base
temp["proxima_revision"] = proxima_revision

flota[placa] = temp