airports = {}

while True:
    print(f"\nAirport Data Management")
    print("1. Enter a new airport")
    print("2. Fetch airport information")
    print("3. Quit")
    valinta = input("Please choose an option (1-3): ")

    if valinta == "1":
        icao = input("Enter the ICAO code: ")
        nimi = input("Enter the airport name: ")
        airports[icao] = nimi
        print(f"Airport {nimi} with ICAO code {icao} has been added.")

    elif valinta == "2":
        icao = input(f"Enter the ICAO code: ")
        if icao in airports:
            print(f"The airport with ICAO code {icao} is {airports[icao]}.")
        else:
            print("No airport found with ICAO code EFHK.")

    elif valinta == "3":
        print(f"Thank you for using the Airport Data Management system. Goodbye!")
        break

    else:
        print("Invalid option. Please try again.")