# DreamHack #1 - Revision #1
# Lesson Name - Fluency: Integers
# Oct 8, 2022

# ===[ CHANGE THESE VALUES BELOW ]===
numbers = "30 6 18 15 13 28 19 3 39 33 10 42"
result = 64

solutions = [[0, 0, 0]]
numbers = numbers.split(" ")
x = 0
for i in numbers:
    numbers[x] = int(i)
    x += 1
x = 0
for a in numbers:
    for b in numbers:
        for c in numbers:
            if a + b + c == result:
                if not any(e in [a, b, c] for e in solutions[x]):
                    solutions.append([a, b, c])
                    x += 1
del solutions[0]
for i in solutions:
    print(f"{i[0]} {i[1]} {i[2]}: {result}")
