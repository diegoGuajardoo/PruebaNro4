productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],

  '2175HD': ['Lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],

  'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],

  'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],

  'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],

  '123FHD': ['Lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],

  '342FHD': ['Lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],

  'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],

}

stock = {

'8475HD': [387990, 10],
'2175HD': [327990, 4],
'JjfFHD': [424990, 1],
'fgdxFHD': [664990, 21],
'123FHD': [290890, 32],
'342FHD': [444990, 7],
'GF75HD': [749990, 2],
'UWU131HD': [349990, 1],
'FS1230HD': [249990, 0]

}

def stock_marca(marca):
    marca = marca.lower()
    encontrados = False
    for modelo, datos in productos.items():
        if datos[0].lower() == marca:
            print(f"modelo: {modelo} - stock: {stock[modelo][1]}")
            encontrados = True
    if not encontrados:
        print("No se encontraron notebooks para esta marca")

def busqueda_precio(p_min, p_max):
    Modelos_en_rango = []
    for modelo, (precio, cantidad) in stock.items():
        if p_min <= precio <= p_max and cantidad > 0:
            marca = productos[modelo][0]
    if Modelos_en_rango:
        for modelo in sorted(Modelos_en_rango):
            print(modelo)
    else:
        print("no hay notebooks en ese rango de precos")
    

def actualizar_precio(modelo, p):
    if modelo in stock:
        stock[modelo][0] = p
        return True
    else:
        return False
    
def menu():
    while True:
        print("/n** Menu principal **")
        print("1  ver por marca stock marca")
        print("2 busqueda por precio")
        print("actializar los precios")
        print("salir")

        opcion = input("selecciona una opcion")
        if opcion == '1':
            marca = input("ingrese la marca")
            stock_marca(marca)
        elif opcion == '2':
            try:
                p_min = int(input("ingrese precio minimo"))
                p_max = int(input("ingrese precio maximo"))
                busqueda_precio(p_min, p_max)
            except ValueError:
                print("debe ingresar numero enteros")
    
       
        elif opcion == '3':
            modelo = input(" ingrese el modelo que para actualizar")
            if modelo not in stock:
                print("el modelo no existe")
                continue
            try:
                nuevos_precios = int(input("ingrese el nuevo precio"))
                actualizado = actualizar_precio(modelo, nuevos_precios)
                if actualizado:
                    print("precios actualizados")
                else:
                    print("la marca no existe")
            except ValueError:
                print("debes ingresar un precio valido")

            respuesta = input("desea actualizar otro precio? (si/no:)").strip.lower()
            if respuesta  != "si":
                continue
        elif opcion == '4':
            print("Menu finalizado")
                