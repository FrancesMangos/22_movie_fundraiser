# IMPORTS GO HERE


# ==================================================
# FUNCTIONS GO HERE
# functions go here
def not_blank(question):
    valid = False

    while not valid:
        response = input(question)

        # checks if name is blank
        if response != "":
            return response
        # prints error message if name is blank
        else:
            print("Cannot be blank!")


def int_check(question):

    error = "Please enter a whole number more than 0"

    valid = False
    while not valid:

        # ask user for age and check if is valid
        try:
            response = int(input(question))

            if response <= 0:
                print(error)
            else:
                return response

        # if an integer is not entered, display an error message
        except ValueError:
            print(error)


# ==================================================
# VARIABLES GO HERE
name = ""

ticket_count = 0

MAX_TICKETS = 5
ticket_sales = 0

# ==================================================
# MAIN PROGRAM STARTS HERE
# execute program if exit code has not been received and there are tickets left
while name != "xxx" and ticket_count < MAX_TICKETS:
    if ticket_count < 4:
        print("You have {} seats "
              "left".format(MAX_TICKETS - ticket_count))

    # warns user that there is only one seat left
    else:
        print("*** There is only ONE seat left! ***")

    # GET DETAILS
    # get name, cannot be blank
    name = not_blank("Name:")
    print()

    # get age between 12 and 130
    age = int_check("Age:")
    print()

    if age < 12:
        print("Sorry - You are too young for this movie.")
        print()
        continue

    if age > 130:
        print("Sorry - Your input is too big, it looks like a mistake")
        print()
        continue

    if age < 16:
        ticket_price = 7.5

    elif age < 65:
        ticket_price = 10.5

    else:
        ticket_price = 6.5

    ticket_count += 1
    print()

if ticket_count == MAX_TICKETS:
    print("You have sold all the available tickets!")
else:
    print("You have sold {} tickets. \n"
          "There are {} places still available"
          .format(ticket_count, MAX_TICKETS - ticket_count))
