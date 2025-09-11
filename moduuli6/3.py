def gallons_to_liters(gallonamäärä):
    return gallonamäärä * 3.785


while True:
    gallonamäärä = float(input("Enter a volume in American gallons (negative value to quit): "))

    if gallonamäärä < 0:
        print("Program finished.")
        break

    result = gallons_to_liters(gallonamäärä)
    print(f"{gallonamäärä} American gallons is {result:.2f} liters.")
