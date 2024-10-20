def main():
    size=int(input("Enter the size of the Square: "))
    print_square(size)

def print_square(size): # Prints a Square of Size x Size
    for i in range(size): # Iterations for Number of Rows - Size
        for j in range(size): # Iterations in a Row = Size
            print("*", end="") # Print * in the same line
        print() # Move to the next line

# (OR)
def main ()
    size=int(input("Enter the size of the Square: "))
    print_square(size)

def print_square(size): # Prints a Square of Size x Size
    for i in range(size): # Iterations for Number of Rows = Size
        print("*" * size) # Print * Size Times

main()
