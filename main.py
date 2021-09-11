print("Hello there!")
print("Welcome to my humble shop")
print("Please select from the following options")
print("L: for List of items")

global apple
global banana
global bread

apple = 6
banana = 6
bread = 8

userIn = input()

if userIn == "L":
    print("You chose to see the list")
    print("We have", "Apples:", apple, "Bananas:", banana, "Bread:", bread)
    print("Type the item you want to buy e.g. Apple, Banana etc")

userIn = input("")

if userIn == "Apple":
    print("How many", userIn)

    buyThis = int(input())
    apple = int(apple-buyThis)
    print("Thank you, now we have", apple, userIn)

elif userIn == "Banana":
    print("How many", userIn)

    buyThis = int(input())
    banana = int(banana-buyThis)
    print("Thank you, now we have", banana, userIn)

elif userIn == "Bread":
    print("How many", userIn)

    buyThis = int(input())
    bread = int(bread-buyThis)
    print("Thank you, now we have", bread, userIn)

else:
    print("You didn't enter L")



