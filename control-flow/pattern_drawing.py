# pattern_drawing.py

# Ask for the pattern size
size = int(input("Enter the size of the pattern: "))

row = 0
while row < size:
    for col in range(size):
        print("*", end="")
    print()  # new line after each row
    row += 1
