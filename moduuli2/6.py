import random

# Generate 3-digit code (0-9)
code_3_digit = ""
for _ in range(3):
    code_3_digit += str(random.randint(0, 9))

# Generate 4-digit code (1-6)
code_4_digit = ""
for _ in range(4):
    code_4_digit += str(random.randint(1, 6))

# Ensure codes are exactly the right length
code_3_digit = code_3_digit.zfill(3)
code_4_digit = code_4_digit.zfill(4)

# Print results
print(f"3-digit code: {code_3_digit}")
print(f"4-digit code: {code_4_digit}")


