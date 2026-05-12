print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?:"))

if height >= 120:
    # print("You can ride the rollercoaster")
    age = int(input("What is your age?:"))
    if age <= 6:
        print("Not allowed on rollercoaster")
    elif age <= 17:
        bill = 17
        print("Youth tickets are 17")
    elif age >= 45 and age <= 55:
        print("you get to ride for free")
    else:
        bill = 27
        print("Adult tickets are 27")

    wants_photo = input("Do you want to have your photo taken? Type y for yes and n for No.")
    if wants_photo == "y":
        #Add $3 to the bill
        print(f"The payment is now ${bill + 3} ")

    if wants_photo == "n":
        print(f"The payment is ${bill}")

else:
    print("Sorry you have to grow taller to ride.")