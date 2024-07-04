import csv 
hotel = []
precio_piso = 0
print = ("bienvenido a hotel, porfavor ingrese en el piso que desee agendar el hotel tiene 5 pisos")
print = ("tambien ingrese el numero de habitacion que desea tiene 8 habitaciones para escoger ")


def reservar_habitacion(hotel):
    try:
        piso = int(input("Ingrese el piso del 1 al 5: "))
        habitacion = int(input("Ingrese el número de la habitación 1 al 8: "))
        if piso >= 1 and piso <= 5 and habitacion >= 1 and habitacion <= 8:
            if hotel[piso-1][habitacion-1]["estado"] == "ocupado":
                print("La habitación ya está ocupada.")
            else:
                hotel[piso-1][habitacion-1]["estado"] = "ocupado"
                print(f"Habitación {habitacion} en el piso {piso} reservada.")
        else:
            print("Habitación no válida.")
    except ValueError:
        print("ingrese un numero valido.")


def buscar_habitacion(hotel):
    try:
        piso = int(input("Ingrese el piso (1 al 5): "))
        habitacion = int(input("Ingrese el número de la habitación 1 al 8: "))
        if piso >= 1 and piso <= 5 and habitacion >= 1 and habitacion <= 8:
            hab = hotel[piso-1][habitacion-1]
            print(f"Habitación {hab['numero']}: Estado - {hab['estado']}, Precio - {hab['precio']}")
        else:
            print("Habitación no válida.")
    except ValueError:
        print("ingrese un numero valido")

def totalizar_ventas(hotel):
    total = 0
    for piso in hotel:
        for habitacion in piso:
            if habitacion["estado"] == "ocupado":
                total += habitacion["precio"]
    print(f"su total de ventas del día es: ${total}")

def guardar_informacion(hotel):
    with open('hotel.txt', 'w') as file:
        for piso in hotel:
            for habitacion in piso:
                file.write(f"Habitación {habitacion['numero']}: Estado - {habitacion['estado']}, Precio - {habitacion['precio']}\n")
    print("Información guardada en hotel.txt")

def menu():
    print(" menu del hotel")
    print("opcion 1 Reservar habitación")
    print ("opcion 2 Buscar habitación")
    print ("opcion 3 Totalizar ventas del día")
    print ("opcion 4 Guardar información en archivo")
    print ("opcion 5 Salir")
    
    opcion = input("Ingrese una opción: ")
    return opcion

while True:
    opcion = menu()
    if opcion == '1':
        reservar_habitacion(hotel)
    elif opcion == '2':
        buscar_habitacion(hotel)
    elif opcion == '3':
        totalizar_ventas(hotel)
    elif opcion == '4':
        guardar_informacion(hotel)
    elif opcion == '5':
        print("Saliendo y guardando datos...")
        guardar_informacion(hotel)
        break
    else:
        print("Opción inválida, por favor intente nuevamente.")