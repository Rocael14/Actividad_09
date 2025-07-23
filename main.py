def Menu():
    print("---Menu---")
    print("1. Registrar Cliente")
    print("2. Listado de Clientes")
    print("3. Salir")



clientes = {}
destinos = {}
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
                            for j in range(cantidad_destinos):
                                codigo_destino = input(f"Ingrese el codigo del destino #{j+1}: ")
                                nombre_destino = input(f"Ingrese el nombre del destino #{j+1}: ")
                                destinos[codigo_destino] = {
                                    "nombre_destino": nombre_destino}
                                clientes[codigo_cliente] = {
                                    "nombre_cliente": nombre_cliente,
                                    "destino": destinos
                                }
                        else:
                            print("No se puedo registrar clientes con mas de 5 viajes o con menos de 1 viaje")
                else:
                    print("No se puedo registrar menos de un cliente")
            case 2:
                print("Listado de Clientes")
                for codigo_cliente, cliente in clientes.items():
                    print(f"Codigo:{codigo_cliente}")
                    print(f"Nombre:{cliente['nombre_cliente']}")
                    for codigo_destino, destino in cliente['destino'].items():
                        print(f"Destino:{destino['nombre_destino']}")
            case 3:
                print("Gracias por utilzar el programa")
            case _:
                print("Opcion invalida")
    except Exception:
        print("Opcion debe ser numerica")