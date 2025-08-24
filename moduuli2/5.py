# Kysytään käyttäjältä syötteet
talents = float(input("Enter talents: "))
pounds = float(input("Enter pounds: "))
lots = float(input("Enter lots: "))

# Muunnoskertoimet
lots_per_pound = 32
pounds_per_talent = 20
grams_per_lot = 13.3

# Lasketaan kokonaispaino grammoina
total_grams = (talents * pounds_per_talent * lots_per_pound * grams_per_lot) + \
              (pounds * lots_per_pound * grams_per_lot) + \
              (lots * grams_per_lot)

# Muunnetaan grammat kilogrammoiksi ja jäljelle jääviksi grammoiksi
kilograms = int(total_grams // 1000)
remaining_grams = total_grams % 1000

# Tulostetaan tulos
print("The weight in modern units:")
print(f"{kilograms} kilograms and {remaining_grams:.2f} grams.")