print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?:"))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age?:"))
    if age <= 6:
        print("Not allowed on rollercoaster")
    elif age <= 17:
        print("Please pay $17")
    else:
        print("Please pay $27")


else:
    print("Sorry you have to grow taller to ride.")