def Menu():
    print("---Menu---")
    print("1. Registrar Cliente")
    print("2. Listado de Clientes")
    print("3. Salir")
def Totalidad_destinos():

while True:
    Menu()
    try:
        opcion = int(input("Selecciona una opcion: "))
        match opcion:
            case 1:
                print("\nRegistrar Cliente")
                cantidad_clientes = int(input("Cuantos clientes desea registrar: "))
                if(cantidad_clientes > 0):
                    for i in range(cantidad_clientes):
                        print(f"\nCliente #{i+1}")
                        codigo_cliente = input("Ingrese el codigo del cliente: ")
                        nombre_cliente = input("Ingrese el nombre del cliente: ")
                        cantidad_destinos = int(input("Cuantos destinos desea registrar (MAX:5): "))
                        if(cantidad_destinos > 0 and cantidad_destinos <= 5):
                            codigo_destino = input(f"Ingrese el codigo del destino #{i+1}: ")
                            nombre_destino = input(f"Ingrese el nombre del destino #{i+1}: ")
            case 2:
                print("Listado de Clientes")
            case 3:
                print("Gracias por utilzar el programa")
            case _:
                print("Opcion invalida")
    except Exception:
        print("Opcion debe ser numerica")