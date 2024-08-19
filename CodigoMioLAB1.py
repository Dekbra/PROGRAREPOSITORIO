class MuestraMedica: #Clase que define las propiedades de cada muestra médica
    def __init__(self, tipo, lote, cantidad, fecha_vencimiento, laboratorio):
        self.tipo = tipo
        self.lote = lote
        self.cantidad = cantidad
        self.fecha_vencimiento = fecha_vencimiento
        self.laboratorio = laboratorio

    def mostrar_info(self): #Método que da formato para mostrar la info de la muestra
        print("-" * 30)
        print(f"Tipo de Muestra: {self.tipo}")
        print(f"Lote: {self.lote}")
        print(f"Cantidad: {self.cantidad}")
        print(f"Fecha de Vencimiento: {self.fecha_vencimiento}")
        print(f"Laboratorio: {self.laboratorio}")
        print("-" * 30)

def ingresar_muestra(): #Función que captura los datos ingresados por el usuario
    print("Seleccione el tipo de muestra médica:")
    print("1. Tazarol Rapid")
    print("2. Neuro Tazarol")
    print("3. Reversal Flex")
    print("4. Dromadol Forte")
    opcion = int(input("Ingrese el número correspondiente al tipo de muestra: "))
    
    if opcion == 1:
        tipo = "Tazarol Rapid"
    elif opcion == 2:
        tipo = "Neuro Tazarol"
    elif opcion == 3:
        tipo = "Reversal Flex"
    elif opcion == 4:
        tipo = "Dromadol Forte"
    else:
        print("Opción no válida. Intente nuevamente.")
        return ingresar_muestra()

    lote = input(f"Ingrese el lote de {tipo}: ")
    cantidad = int(input(f"Ingrese la cantidad recibida de {tipo}: "))
    fecha_vencimiento = input(f"Ingrese la fecha de vencimiento de {tipo} (dd/mm/yyyy): ")
    laboratorio = input(f"Ingrese el laboratorio fabricante de {tipo}: ")

    return MuestraMedica(tipo, lote, cantidad, fecha_vencimiento, laboratorio)

# Lista para almacenar todas las muestras ingresadas
muestras = []

def mostrar_muestras(): #Función para mostrar todas las muestras registradas
    print("\nMuestras médicas registradas:")
    for muestra in muestras:
        muestra.mostrar_info()

def menu_principal(): #Menú principal para navegar entre las opciones
    while True:
        print("Ingrese la opción que desea realizar:")
        opcion = int(input("1. Ingresar muestra médica\n2. Mostrar muestras\n3. Salir\n"))
        
        if opcion == 1:
            nueva_muestra = ingresar_muestra()
            muestras.append(nueva_muestra)
        elif opcion == 2:
            mostrar_muestras()
        elif opcion == 3:
            print("Gracias por utilizar el sistema.")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

menu_principal() #Ejecutar el menú principal
