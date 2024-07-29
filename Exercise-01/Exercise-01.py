# Q1: Age Assignments Based on the Riddle
# Problem Statement: Write a program to solve this age-related riddle! Anton, Beth, Chen, Drew, and Ethan are all friends. Their ages are as follows:
# Anton is 21 years old.
# Beth is 6 years older than Anton.
# Chen is 20 years older than Beth.
# Drew is as old as Chen's age plus Anton's age.
# Ethan is the same age as Chen.
# Your code should store each person's age to a variable and print their names and ages at the end.
# Anton is 3
# Beth is 4
# Chen is 5
# Drew is 6
# Ethan is 7

anton: int = 21

beth: int = anton + 6

chen: int = beth + 20

drew: int = chen + anton

ethan: int = chen

ages: dict[str, int] = {"Anton": anton, "Beth": beth, "Chen": chen, "Drew": drew, "Ethan": ethan}

for name, age in ages.items():
    print(f"{name} is {age} years old.")