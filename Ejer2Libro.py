class Articulo: #Clase que guarda el tipo, marca, precios y tiene el método para mostrar la info
    def __init__(self, tipo, marca, precio_compra, precio_venta):
        self.tipo = tipo
        self.marca = marca
        self.precio_compra = precio_compra
        self.precio_venta = precio_venta

    def mostrar_info(self): #Método que da formato y muestra la información del artículo
        print(f"Artículo: {self.tipo}")
        print(f"Marca: {self.marca}")
        print(f"Precio de Compra: ${self.precio_compra}")
        print(f"Precio de Venta: ${self.precio_venta}")
        print("-" * 30)

def calcular_precio_venta(precio_compra, margen=1.30): #Fórmula para calcular el precio de venta con margen estándar
    return precio_compra * margen

def ingresar_articulo(): #Captura de datos con opciones predefinidas
    print("Seleccione el tipo de artículo que desea registrar:")
    print("1. Cuaderno")
    print("2. Lápiz")
    opcion = int(input("Ingrese el número correspondiente al tipo de artículo: "))
    
    if opcion == 1:
        tipo = input("Ingrese el tipo de cuaderno (e.g., '50 hojas', '100 hojas'): ")
        marca = "HOJITAS"
    elif opcion == 2:
        tipo = input("Ingrese el tipo de lápiz (e.g., 'grafito', 'colores'): ")
        marca = "RAYAS"
    else:
        print("Opción no válida. Por favor, intente de nuevo.")
        return ingresar_articulo()

    precio_compra = float(input(f"Ingrese el precio de compra para {tipo} ({marca}): "))
    precio_venta = calcular_precio_venta(precio_compra)
    return Articulo(tipo=tipo, marca=marca, precio_compra=precio_compra, precio_venta=precio_venta)

# Lista para almacenar todos los artículos ingresados
articulos = []

# Bucle que permite registrar más de un artículo hasta que el usuario decida parar
while True:
    articulos.append(ingresar_articulo())
    
    continuar = input("¿Desea ingresar otro artículo? (s/n): ").strip().lower()
    if continuar == 'n':
        break

# Despliega toda la información de los artículos que se registraron
print("\nArtículos registrados:")
for articulo in articulos:
    articulo.mostrar_info()





    
   