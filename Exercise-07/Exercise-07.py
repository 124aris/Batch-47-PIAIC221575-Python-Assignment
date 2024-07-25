# Q7: String Stripping and Justifying
# Task: Given the string s, use string methods to:
# Remove leading/trailing spaces: remove all leading and trailing whitespace characters from the string.
# Left justify with '*': left justify the string within a field of width 20, using * as the fill character.
# Right justify with '*': right justify the string within a field of width 20, using * as the fill character.
# s:str ="   Python is fun!   "
# Expected Output:
# Python is fun!
# Python is fun!*****
# *****Python is fun!

s: str = "   Python is fun!   "

strip_s = s.strip()

ljust_s = strip_s.ljust(20, '*')

rjust_s = strip_s.rjust(20, '*')

print(strip_s)

print(ljust_s)

print(rjust_s)