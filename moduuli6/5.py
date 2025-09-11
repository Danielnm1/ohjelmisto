def filter_even_numbers(kokonaislukujen_lista):
    evens = []
    for luku in kokonaislukujen_lista:
        if luku % 2 == 0:
            evens.append(luku)
    return evens


b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = filter_even_numbers(b)

print("Original list:", b)
print("List with even numbers only:", even)
