# Prompting the user to enter a height.
while True:
    height_str = input("Height: ")
    # Checking if the height is a numerical character.
    if height_str.isdigit():
        n = int(height_str)
        if 1 <= n <= 8:
            break
# Printing out the half pyramid with the required height
for i in range(n):
    for j in range(n):
        if i + j < (n - 1):
            print(" ", end="")
        else:
            print("#", end="")
    print()
