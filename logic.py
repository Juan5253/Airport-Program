#Print menu options 
def menuView():
    title = "BIENVENIDO"
    print(title.center(20))
    print("-Elija la acción que desea realizar- \n 1.)Agregar Pasajero\n 2.)Agregar ciudad\n 3.)Ver destino pasajero\n 4.)Ver cantidad viajeros a destino especificado\n 5.) --Salir--")
#Get the values of new Passenger and returns a tuple
def addPassenger():
    name = input("Digite el nombre del pasajero: ")
    dni = int(input("Digite el DNI del pasajero: "))
    destiny = input("Digite la ciudad de destino: ")
    return ((name, dni, destiny))
#Get the values of new Country and returns a tuple    
def addCountry():
    country = input("Digite el Pais de origen : ")
    city = input("Digite la Ciudad de origen: ")
    return ((country, city))

