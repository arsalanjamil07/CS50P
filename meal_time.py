def main()
    time_str = input("What time is it e.g 7:30? ")
    time_float = covert(time_str)

    if time_float >=7.0 and time_float <=8.0:
        print("Breakfast Time")
    elif time_float >=12.0 and time_float <=13.0:
        print("Lunch Time")
    elif time_float >=18.0 and time_float <=19.0:
        print("Dinner Time")
    else:
        print("No Meal Time")

def convert(t):
    hours, minutes = t.split(":")
    return float(hours) + float(minutes)/60

maint()

# Splitting the Input but assigning Variables in Seperate Lines

def convert(t):
    time_parts = t.split(":")
    hours = time_parts[0]
    minutes = time_parts[1]
    return float(hours) + float(minutes)/60
