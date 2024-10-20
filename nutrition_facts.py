def main():
    fruit = input("Fruit: ")
    output = calories(fruit)
    print("Calories:",output)

def calories(f):
    list={"A":20,"B":20,"C":30}
    for i in list:
        if f==i:
            return list[i]
          
main()
