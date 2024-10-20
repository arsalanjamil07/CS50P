def main():
    dollars = dollars_to_float(input("How much was the Meal? "))
    percent = percent_to_float(input("What percent would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

def dollars_to_float(d:
    # Remove the leading $ and convert to float
    return float(d.replace("$", ""))

def percent_to_float(p):
    # Remove the trailing % and convert to float
    return float(p.replace("%", "")) / 100

main()
