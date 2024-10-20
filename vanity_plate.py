def main():
    plate = input("Enter Vanity Plate: ").upper()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if s[:2].isalpha():                                 # Check if the first two characters are letters
        if 2 <= len(s) <= 6:                            # Check if the length of the string is between 2 and 6
            
            has_number = False                          # Initialize a flag to check if a number has been encountered
            for char in s:                              # Iterate through the string
                if char.isdigit():                      # Check if the character is a digit
                    if char == '0' and not has_number:  # If the digit is '0' and it's the first number, return False
                        return False 
                    has_number = True                   # Set the flag to True as a number has been encountered
                elif has_number:                        # If a letter is found after a number, return False
                    return False    
                                                        # Moved to this next part because False has not been returned 
            if s.isalnum():                             # Check if the string is alphanumeric
                return True                             # If all conditions are met, return True
    return False

main()
