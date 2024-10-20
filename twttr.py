string = input("Enter a String: ")

new_string = ""
for i in string:
    if i in ["a", "e", "i", "o", "u"]:
        new_string = new_string
    else:
        new_string = new_string + i

print("Output: ", new_string)
