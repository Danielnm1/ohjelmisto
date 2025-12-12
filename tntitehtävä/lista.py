import random
def sum_squares():
    first,second = random.randint(1,6), random.randint(1,6)
    return first,second
die1,die2 =sum_squares()
result = sum_squares(die1,die2)
print(result)

