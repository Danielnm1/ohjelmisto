names = set()
name = input("Enter name or (press enter to quit): ")
while name != "":
    if name in names:
        print("Existing name")
    else:
        print("New name")
    names.add(name)
    name = input("Enter name or (press enter to quit): ")
print("\nNames entered:")
for name in names:
    print(names)