#AIRPORT PROGRAM
import logic
from os import system
passengers = []
country = []
option=0
while option != 5:
    logic.menuView()
    option = int(input())
    if option == 1:
        system("cls")
        newPassenger=logic.addPassenger()
        passengers.append(newPassenger)
    elif option == 2:
        system("cls")
        newCountry=logic.addCountry()
        country.append(newCountry)
    elif option == 3:
        system("cls") 
        dni = int(input("Digite el DNI del pasajero: "))
        for i in range(len(passengers)): #Iterate through the rows of the passengers array
            if passengers[i][1] == dni: #As the dni of the passenger is in position 1 of the tuple, it is compared with the dni of parameter
                destiny = passengers[i][2] #if the dni coincides, the value in position i of the list, and 2 in the tuple (for format, see statement) is saved in the destination variable
                print (destiny)
    elif option == 4:
        system("cls")
        country = input("Digite el pais: ")
        count=0 #passenger counter
        for i in range(len(passengers)): #Iterate through the rows of the passengers array
            count+=passengers[i][2].count(country) #Use count method to Returns the number of times a specified value occurs in a tuple, and added to the counter
        print("La cantidad de viajeros hacia " + country + " es: " + str(count)) #exit for and print the counter
            
    
    
    


    