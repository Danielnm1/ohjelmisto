# Luodaan hahmon inventaario
inventaario = []

# Lisätään tavaroita inventaarioon
inventaario.append({"nimi": "erinomainen", "hyvä": "surkea"})
inventaario.append({"nimi": "kilpi", "laatu": "ok"})
inventaario.append({"nimi": "surkea", "laatu": "hyvä"})

# Tulostetaan inventaario
print("Hahmon tavarat:")
for tavara in inventaario:
    print(f"- {tavara['nimi']} ({tavara['hyvä']})")

# Esimerkki käytöstä: jos hahmolla on miekka, tehdään jotain
onko_miekka = any(tavara["nimi"] == "miekka" for tavara in inventaario)

if onko_miekka:
    print("Hahmolla on miekka! Valmistaudu taisteluun.")
else:
    print("Hahmolla ei ole miekkaa.")
