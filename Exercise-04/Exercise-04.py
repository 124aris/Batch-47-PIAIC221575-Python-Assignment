# Q4: Substring Search
# Task: Given the string s, use string methods to:
# Find the index of "fox": get the starting index of the substring "fox". If "fox" is not found, it should return -1.
# Count occurrences of "the": Use the string's built-in method to count how many times the substring "the" appears in the string.
# s:str ="the quick brown fox jumps over the lazy dog"
# Expected Output:
# index of 'fox' is 16
# 'the' appears 2 times

s: str = "the quick brown fox jumps over the lazy dog"

index = s.find("fox")

count = s.count("the")

print(f"index of 'fox' is {index}")

print(f"'the' appears {count} times")