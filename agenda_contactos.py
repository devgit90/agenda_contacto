def mostrar_menu():
    print("-- Agenda de contactos --")
    print("1.- Agregar contacto")
    print("2.- Eliminar contacto")
    print("3.- Buscar contacto")
    print("4.- Lista contacto")
    print("5.- Salir contacto")

def agregar_contacto(agenda):
    nombre= input("Por favor introduzca el nombre")
    telefono = input("Por favor introduzca el teléfono")
    email = input("Por favor introduzca el email")

    agenda[nombre] = {"telefono":telefono, "email":email}

    print(f"Se ha agregado el contacto {nombre} exitosamente")

def eliminar_contacto(agenda):
    nombre= input("Por favor introduzca el nombre de la agenda a eliminar")
    if nombre in agenda:
        del agenda[nombre]
        print(f"El contacto de {nombre} ha sido eliminado ")
    else:
        print(f"No se ha encontrado nombre {nombre}")

def buscar_contacto(agenda):
    nombre= input("Por favor introduzca el nombre de la agenda a buscar")
    if nombre in agenda:
        print(f"Nombre: {nombre}")
        print(f"Teléfono: {agenda[nombre]['telefono']}")
        print(f"Email: {agenda[nombre]['email']}")
    else:
        print(f"El contacto {nombre} no ha sido encontrado en la agenda")

def listar_contactos(agenda):
    if agenda:
        print("Lista de contactos")
        for nombre,info in agenda.items():
            print(f"Nombre: {nombre}")
            print(f"Teléfono: {info["telefono"]}")
            print(f"Email: {info["email"]}")

            print("-" * 20)
    else:
        print("La agenda aún está vacía")

def agenda_contactos():
    agenda = {}

    while True:
        mostrar_menu()
        opcion = input("Por favor elija una opción: ")

        if opcion == "1":
            agregar_contacto(agenda)
        elif opcion == "2":
            eliminar_contacto(agenda)
        elif opcion == "3":
            buscar_contacto(agenda)
        elif opcion == "4":
            listar_contactos(agenda)
        elif opcion == "5":
            print("Saliendo de la agenda de contactos")
            break
        else:
            print("POr favor seleccione una opción válida")
        
agenda_contactos()