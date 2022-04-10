# Directions
location = ["seas", "mountains", "forest"]
yes_no = ["yes", "no"]
directions = ["left", "right", "forward", "backward"]
cave_directions = ["left", "forward", "backward"]
wall_directions = ["right", "forward", "backward"]

# Introduction
name = input("What is your name, adventurer?\n")
name = name.title()
print("Greetings, " + name + ". Let us go on a quest!")

print()
answer = ""
while answer not in yes_no:
    answer = input("Are you ready for an adventure?\n"
                   "Yes or No?").lower()
    if answer == "yes":
        print("Woohoo! Let's go!")
    elif answer == "no":
        print("Well okay then. I wasted my time. Goodbye, " + name + ".")
        quit()
    else:
        print("I did not understand that!\n")

print()
answer = ""
while answer not in location:
    answer = input("Which area would you like to travel?\n"
                   "The seas, the mountains, or the forest?").lower()
    if answer == "seas":
        print("You do not have a boat so you try and swim instead. You sadly drown."
              " Farewell, " + name + ".")
        quit()
    elif answer == "mountains":
        print("You think you're doing well but unfortunately lose your grip and fall"
              " Farewell, " + name + ".")
        quit()
    elif answer == "forest":
        print("You head into the forest!")
    else:
        print("I did not understand that!\n")

print()
answer = ""
start = False
while answer not in directions and not start:
    print("Left is a rocky wall.")
    print("Forward is a group of sleeping bears.")
    print("Right is a gloomy cave.")
    print("Backward leads outside the forest\n")
    answer = input("Which direction would you towards? Left, Forward, Right or Backward?").lower()
    if answer == "left":
        print("You climb up the rocky wall.")
        answer = "rocky_wall"
        start = True
    elif answer == "forward":
        print("You head towards the sleeping bears. You wake them up and sadly die."
              " Farewell, " + name + ".")
    elif answer == "right":
        print("You head inside the gloomy cave.")
        answer = "gloomy_cave"
        start = True
    elif answer == "backward":
        print("Well okay then. I wasted my time. Goodbye, " + name + ".")
        quit()
    else:
        print("I did not understand that!\n")

print()
if answer == "gloomy_cave":
    print("You are inside the gloomy cave")
    print("Left is a giant pool of water")
    print("Forward is a long passageway")
    print("Backwards is the entrance of the cave")
elif answer == "rocky_wall":
    print("You are at the top of the rock wall")




