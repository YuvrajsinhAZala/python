rows = 5
letter = 65

for i in range(1, rows + 1):

    for j in range(i):
        print(chr(letter), end="")

    letter = letter + 1
    print()