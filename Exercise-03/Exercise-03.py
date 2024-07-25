# Q3: String Manipulation
# Task: Given the string s, use string methods to:
# Capitalize the first letter: make the first character uppercase and the rest of the string lowercase.
# Convert to uppercase: change all characters in the string to uppercase.
# Convert to lowercase: change all characters in the string to lowercase.
# s:str = "hElLo WoRlD"
# Expected Output:
# Hello world
# HELLO WORLD
# hello world

s: str = "hElLo WoRlD"

capitalize_s: str = s.capitalize()

upper_s: str = s.upper()

lower_s: str = s.lower()

print(capitalize_s)

print(upper_s)

print(lower_s)