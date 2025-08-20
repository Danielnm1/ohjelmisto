# Keskiaikaisten mittojen muunnos kiloiksi ja grammoiksi

# Vakioarvot
LUOTI_GR = 13.3
NAULA_LUOTI = 32
LEIVISKA_NAULA = 20

# Kysytään käyttäjältä (sallitaan desimaalit)
leiviskat = float(input("Anna leiviskät: "))
naulat = float(input("Anna naulat: "))
luodit = float(input("Anna luodit: "))

# Lasketaan kokonaisluodit
kokonaisluodit = leiviskat * LEIVISKA_NAULA * NAULA_LUOTI \
               + naulat * NAULA_LUOTI \
               + luodit

# Muutetaan grammoiksi
grammat = kokonaisluodit * LUOTI_GR

# Erotellaan kilogrammat ja ylimääräiset grammat
kilot = int(grammat // 1000)
grammat = grammat % 1000

# Tulostus
print(f"Massa nykymittojen mukaan: {kilot} kilogrammaa ja {grammat:.2f} grammaa")