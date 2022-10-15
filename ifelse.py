print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height>=120: 
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age<12:
        print("Ticket price= $5")
    elif age<=18:
        print("Ticket price= $10")
    else:
        print("Ticket price= $12")

else:
     print("Sorry, you cannot ride the rollercoaster.")
