# variables go here
name = ""
count = 0
MAX_TICKETS = 5

# execute program if exit code has not been received and there are tickets left
while name != "xxx" and count < MAX_TICKETS:
    print("You have {} seats "
          "left".format(MAX_TICKETS - count))

    name = input("Name:")
    count += 1
    print()

if count == MAX_TICKETS:
    print("You have sold all the available tickets!")
else:
    print("You have sold {} tickets. \n"
          "There are {} places still available"
          .format(count, MAX_TICKETS - count))
