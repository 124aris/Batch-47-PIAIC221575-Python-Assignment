# Q10: Round floating-point numbers
# Task: Given a floating-point number value
# Round value to the nearest integer.
# Round value to two decimal places.
# value:float = 12.34567
# Expected Output:
# Rounded to nearest integer: 12
# Rounded to two decimal places: 12.35

value: float = 12.34567

rounded_value = round(value)

decimals_value = round(value, 2)

print(f"Rounded to nearest integer: {rounded_value}")

print(f"Rounded to two decimal places: {decimals_value}")