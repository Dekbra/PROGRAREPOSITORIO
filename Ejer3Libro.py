class Auto: #Clase para crear autos y guardar sus características
    def __init__(self, modelo,tipo, marca, ano, kilometraje, precio_venta, color, transmision, placa, traccion):
        self.modelo = modelo
        self.tipo = tipo
        self.marca = marca
        self.ano = ano
        self.precio_venta = precio_venta
        self.color = color
        self.kilometraje = kilometraje
        self.transmision = transmision
        self.placa = placa
        self.traccion = traccion
        self.capacidad = "5 pasajeros"
        self.ruedas = "4 ruedas"

    def mostrar_info(self): #Muestra toda la info del auto formateada
        print("-" * 30)
        print(f"Modelo: {self.modelo}")
        print(f"Marca: {self.marca}")
        print(f"Tipo: {self.tipo}")
        print(f"Año: {self.ano}")
        print(f"Color: {self.color}")
        print(f"Capacidad: {self.capacidad}")
        print(f"Ruedas: {self.ruedas}")
        print(f"Transmisión: {self.transmision}")
        print(f"Placa: {self.placa}")
        print(f"Kilometraje: {self.kilometraje}")
        print(f"Precio de Venta: ${self.precio_venta}")
        print("-" * 30)

def ingresar_autos(): #Captura la info del auto ingresado por el usuario
    modelo = input("Ingrese el modelo del auto: ")
    tipo = input("Ingrese el tipo del auto: ")
    marca = input("Ingrese la marca del auto: ")
    ano = int(input("Ingrese el año del auto: "))
    kilometraje = int(input("Ingrese el kilometraje del auto: "))
    precio_compra = float(input(f"Ingrese el precio de compra del auto {modelo}: $"))
    color = input("Ingrese el color del auto: ")
    transmision = input("Ingrese la transmisión del auto: ")
    placa = input("Ingrese la placa del auto: ")
    traccion = input("Ingrese la tracción del auto: ")
    precio_venta = calcular_precio_venta(precio_compra)
    return Auto(modelo, tipo, marca, ano, kilometraje, precio_venta, color, transmision, placa, traccion)

def calcular_precio_venta(precio_compra, margen=1.4): #Calcula el precio de venta basado en un margen
    precio_venta = precio_compra * margen
    return precio_venta

# Lista global para almacenar los autos ingresados
autos = []

def mostrar_autos(autos): #Recorre y muestra todos los autos registrados
    print("\nAutos registrados:")
    for autos in autos:
        autos.mostrar_info()

def menu_principal(): #Menú principal con opciones para ingresar, mostrar autos o salir
    while True:
        opcion = int(input("Ingrese la opción que desea hacer: \n Opción 1: Ingresar auto \n Opción 2: Mostrar Autos \n Opción 3: Salir \n"))
        if opcion == 1:
            nuevo_auto = ingresar_autos()
            autos.append(nuevo_auto)
        elif opcion == 2:
            mostrar_autos(autos)
        if opcion == 3:
            print("Gracias por utilizar el sistema")
            break

menu_principal() #Ejecutar la función del menú principal

            




   