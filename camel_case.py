def main():
    camel_case_input = input("Enter a Camel Case Variable Name: ")
    snake_case_output = camel_to_snake(camel_case_input)
    print("Snake Case Variable Name: ", snake_case_output)

def camel_to_snake(camel_case):
    snake_case = ""
    for char in camel_case: # Iterating through each character in the String like List
        if char.isupper():
            snake_case = snake case + "_" + char.lower()
        else:
            snake_case = snake_case + char
    return snake_case

main()
