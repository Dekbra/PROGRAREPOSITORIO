class dispositivo: #Clase que define las propiedades del dispositivo y tiene método para mostrar la info
    def __init__(self, marca, modelo, anofabricacion, paisproveniencia, precio_venta, resolucion):
        self.marca = marca
        self.modelo = modelo
        self.anofabricacion = anofabricacion
        self.paisproveniencia = paisproveniencia
        self.precio_venta = precio_venta
        self.resolucion = resolucion
        
    def mostrar_info(self): #Formato para mostrar la información del dispositivo en pantalla
        print("-" * 30)
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Año Fabricación: {self.anofabricacion}")
        print(f"País de Proveniencia: {self.paisproveniencia}")
        print(f"Precio de venta: ${self.precio_venta}")
        print(f"Resolución: {self.resolucion}")
        print("-" * 30)

def ingresar_datos(): #Captura de datos del dispositivo por parte del usuario
    marca = input("Ingrese la marca del dispositivo: ")
    modelo = input("Ingrese el modelo del dispositivo: ")
    anofabricacion = input("Ingrese el año de fabricación del dispositivo: ")
    paisproveniencia = input("Ingrese el país de proveniencia del dispositivo: ")
    precio_compra = float(input("Ingrese el precio de compra del dispositivo: $"))
    precio_venta = calcular_precio_venta(precio_compra)
    resolucion = input("Ingrese la resolución de la pantalla del dispositivo: ")
    return dispositivo(marca, modelo, anofabricacion, paisproveniencia, precio_venta, resolucion)

def calcular_precio_venta(precio_compra, margen=1.7): #Calcula el precio de venta con margen fijo
    precio_venta = precio_compra * margen
    return precio_venta

dispositivos = [] #Lista global para almacenar los dispositivos registrados

def mostrar_dispositivos(dispositivos): #Muestra todos los dispositivos registrados
    print("\nDispositivos registrados:")
    for dispositivo in dispositivos:
        dispositivo.mostrar_info()

def menu_principal(): #Función que ejecuta el menú principal con las opciones del sistema
    print("-" * 30)
    while True:
        opcion = int(input("Ingrese la opción que desea hacer: \n Opción 1: Ingresar dispositivo \n Opción 2: Mostrar dispositivos \n Opción 3: Salir \n"))
        if opcion == 1:
            nuevo_dispositivo = ingresar_datos()
            dispositivos.append(nuevo_dispositivo)
        elif opcion == 2:
            mostrar_dispositivos(dispositivos)
        if opcion == 3:
            print("Gracias por utilizar el sistema")
            break
        print("-" * 30)

menu_principal() #Iniciar el sistema con el menú principal
