vuosi_luku = int(input("Anna vuosiluku: "))
jaollinen_neljalla = vuosi_luku % 4 == 0
jaollinen_sadalla = vuosi_luku % 100 == 0
jaollinen_neljasadalla = vuosi_luku % 400 == 0
if jaollinen_neljalla == False:
    print(f"Vuosi {vuosi_luku} ei ole karkausvuosi.")
elif jaollinen_neljalla == True and jaollinen_sadalla == True and jaollinen_neljasadalla == False:
    print(f"Vuosi {vuosi_luku} ei ole karkausvuosi.")
elif jaollinen_neljalla == True and jaollinen_sadalla == True :
     print(f"Vuosi {vuosi_luku} on karkausvuosi.")
elif jaollinen_neljalla == True and jaollinen_sadalla == False and jaollinen_neljasadalla == True:
    print(f"Vuosi {vuosi_luku} on karkausvuosi.")







