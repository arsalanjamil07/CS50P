while True:
    try:
        fraction = input("What's the Fraction? ")
        x, y = fraction.split("/")
        x = int(x)
        y = int(y)
        z = x/y*100
        if y == 0:
            raise ZeroDivisionError
        if x > y:
            raise ValueError
        if z<1:
            print("E")
        elif z>99:
            print("F")
        else:
            print(f"{z:.1f}")
        break
    except ValueError:
        pass
    except ZeroDivisionError:
        pass
