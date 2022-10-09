# DreamHack #1 - Revision #2
# Lesson Name - Fluency: Integers
# Date Created: Oct 8, 2022
print('''
DreamHack #1 - Revision #1
Lesson Name - Fluency: Integers
Date Created: Oct 8, 2022
https://github.com/TechDudie/DreamHack
Disclaimer: I wrote this in 15 minutes so bugs are expected.
'''.strip())
two = True
mode = input("Sum of 2 or 3 numbers? ")
if mode == "3":
    two = False
mode = int(mode)
while True:
    numbers = input("List of numbers: ")
    result = int(input("Sum: "))
    solutions = []
    for i in range(0, mode):
        solutions.append(0)
    solutions = [solutions]
    print(solutions)
    numbers = numbers.split(" ")
    x = 0
    for i in numbers:
        numbers[x] = int(i)
        x += 1
    x = 0
    print("Calculating...")
    if two:
        for a in numbers:
            for b in numbers:
                if a + b == result:
                    if not any(e in [a, b] for e in solutions[x]):
                        solutions.append([a, b])
                        x += 1
        del solutions[0]
        for i in solutions:
            print(f"{i[0]} + {i[1]} = {result}")
    else:
        for a in numbers:
            for b in numbers:
                for c in numbers:
                    if a + b + c == result:
                        if not any(e in [a, b, c] for e in solutions[x]):
                            solutions.append([a, b, c])
                            x += 1
        del solutions[0]
        for i in solutions:
            print(f"{i[0]} + {i[1]} + {i[2]} = {result}")
