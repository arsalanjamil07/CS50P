print("Amount due: 50")
amount_due = 50

while amount_due!=0:
    coin=int(input("Insert a Coin: "))
    if coin==25 or coin==10 or coin==5:   # Same as, if coin in [25, 10, 5]:
        amount_due -= coin                # Same as, amount_due=amount_due-coin
        if amount_due>0:
            print("Amount due: ", amount_due)
        else:
            print("Change Owed: ", -amount_due)
    else:
        print("Amount due: ", amount_due)
