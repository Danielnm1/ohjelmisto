luku = int(input("Anna luku: "))

if luku < 2:
    print("Luku ei ole alkuluku")
else:
    on_alkuluku = True
    for n in range(2, luku):
        if luku % n == 0:
            on_alkuluku = False
            print("Ei ole alkuluku")
            break
    if on_alkuluku:
        print("On alkuluku")


