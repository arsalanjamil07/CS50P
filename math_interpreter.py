expression = input("Enter an arithematic expression (e.g 1+1): ").strip()
x, y, z = expression.split() # Will assign 1 to x, + to y and 1 to z
x = int(x)
z = int(z)

if y == "+":
    result = x + z
elif y == "-":
    result = x - z
elif y == "*":
    result = x * z
elif y == "/":
    result = x / z

print(f"{Result:.1f}")
