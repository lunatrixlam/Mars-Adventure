# Mars Adventure is an interactive text adventure game about traveling to the planet Mars. We will practice capturing user input, producing dynamic output, using conditional statements and comparison operators, and converting data types!

# Welcome the user
print("Welcome to your Mars Adventure!")
print()

# Get user name and ask if they are excited
name = input("What is your name? ").title().strip()
print()
print(f"Hello, {name}! We are going to have a great time. Are you excited? (Enter Y or N).")
print()

# Get user response and respond with output
excited = input("> ").upper().strip()

if excited == "Y":
    print("Great, I knew you'd say that!")
elif excited == "N":
    print("Well, it's too late to back out now...")
else:
    print("That wasn't an option but you're here so let's go!")

# Ask user how many suitcases they'd like to bring
print()
print("It's time to pack for your trip to Mars.")
print()

while True:
    print("How many suitcases do you plan to bring?")
    num_suitcases = int(input("> "))
    
    if num_suitcases > 2:
        print("Oh, that is far too many! Our spaceship can't handle that. Let's try again.")
        print()
    else:
        print("Perfect! Your suitcases will fit in our spaceship!")
        break

# Invite user to bring their animal companion 
print()
print("You are allowed to bring your best animal pal with you.")

type_animal = input("What type of pal will you bring? ")

name_animal = input("What is the name of your best pal? ").title().strip()

print()
print(f"Cool! You are bringing {name_animal}, who is a {type_animal}.")

# Ask user their interior decor preference
print()
print("Great news. NASA's interior design team will decorate your spaceship!")
print()
print("You have a couple of options for the interior decor:")
print("Option A: Sleek, modern minimalism")
print("Option B: Retro, vintage space age")
print("Option C: SF hippie chic")

print()
decor = input("Which option do you prefer? (Enter A, B, or C) ").upper().strip()

if decor == "A":
    decor = "modern minimalist"
elif decor == "B":
    decor = "vintage space"
elif decor == "C":
    decor = "hippie chic"

print()
print("I can see it now: ")
print(f"{name} and {name_animal} surfing the celestial abyss...")
print(f"in a {decor} shapeship!")
print()

# Countdown to liftoff at 1200 degrees

import time

temperature = 0 

print("Lift-off permitted at 1200 degrees.")
print()

while temperature < 1200: 
    print(f"The current temperature is: {temperature}")
    time.sleep(2)
    temperature += 100

print()

# Countdown to liftoff and use the time module's sleep function to pause the countdown based on the specified number of seconds

print("We are now preparing for lift-off in:")

timer = 5

while timer > 0:
    print(timer, "...")
    time.sleep(2)
    timer -= 1

print("*** LIFT OFF! ***")
print()

# Use turtle Module to draw five stars upon lift-off

import turtle

wn = turtle.Screen()
wn.bgcolor("black")
frank = turtle.Turtle()

frank.color("yellow")

for i in range(3):
    
    i = 0
    while i < 5:
        frank.forward(20)
        frank.left(144)
        i += 1
    
    frank.penup()
    frank.forward(50)
    frank.left(120)
    frank.pendown()

frank.penup()
frank.right(135)
frank.forward(100)
frank.right(45)
frank.pendown()

frank.color("white")

for i in range(359):
    frank.forward(50)
    frank.backward(50)
    frank.right(1)

frank.penup()
frank.backward(20)
frank.right(72)
frank.forward(20)
frank.pendown()

frank.color("black")

for i in range(359):
    frank.forward(50)
    frank.backward(50)
    frank.right(1)

frank.penup()
frank.forward(150)
frank.right(72)
frank.pendown()

frank.color("white")

frank.write(f"Welcome to Mars, {name} and {name_animal}!")

# Ask user which planet they'd like to visit
print("Which planet would you like to visit?")
planet = input("> ").lower().strip()
print()

if planet == "saturn":
    print("Sorry, the spaceship for Saturn left last week.")
elif planet == "venus":
    print("Venus? It's really not worth the trip.")
elif planet == "mercury":
    print("This is not the right season to visit Mercury.")
else:
    print("Hm... that's not a bad suggestion but Mars is way more interesting!")

print()

print("Click anywhere among the moon and stars to return to earth.")

wn.exitonclick()