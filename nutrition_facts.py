def main():
    fruit = input("Fruit: ")
    output = calories(fruit)
    print("Calories:",output)

def calories(f):
    dict={"A":20,"B":20,"C":30}
    for i in dict:
        if f==i:
            return dict[i]
          
main()
