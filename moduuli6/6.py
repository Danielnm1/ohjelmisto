import math

def calculate_unit_price(d, p):
    return p / (math.pi * (d / 200) ** 2)

d1 = float(input("Enter the diameter of the first pizza (cm): "))
p1 = float(input("Enter the price of the first pizza (euros): "))
d2 = float(input("Enter the diameter of the second pizza (cm): "))
p2 = float(input("Enter the price of the second pizza (euros): "))

u1 = calculate_unit_price(d1, p1)
u2 = calculate_unit_price(d2, p2)

print(f"Unit price of the first pizza: {u1:.2f} euros/m²")
print(f"Unit price of the second pizza: {u2:.2f} euros/m²")

if u1 < u2:
    print("The first pizza provides better value for money.")
elif u2 < u1:
    print("The second pizza provides better value for money.")
else:
    print("Both pizzas provide the same value for money.")
