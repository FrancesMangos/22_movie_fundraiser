# IMPORTS GO HERE
import re
import pandas

# ==================================================
# FUNCTIONS GO HERE


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
            print()


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


def check_tickets(tickets_sold, ticket_limit):
    # tells user how seats are left
    if tickets_sold < ticket_limit - 1:
        print("You have {} seats "
              "left".format(ticket_limit - tickets_sold))

    else:
        print("*** There is only ONE seat left! ***")

    return ""


def get_ticket_price():
    age = int_check("Age:")
    print()

    if age < 12:
        print("Sorry - You are too young for this movie.")
        print()
        return "invalid ticket price"

    if age > 130:
        print("Sorry - Your input is too big, it looks like a mistake")
        print()
        return "invalid ticket price"

    if age < 16:
        ticket_price = 7.5

    elif age < 65:
        ticket_price = 10.5

    else:
        ticket_price = 6.5

    return ticket_price

# ==================================================
# VARIABLES GO HERE


MAX_TICKETS = 5

name = ""

ticket_count = 0
ticket_sales = 0

# ==================================================
# DATAFRAME STUFF GOES HERE

all_names = []
all_tickets = []

movie_data_dict = {
    'Name': all_names,
    'Ticket': all_tickets
}

# ==================================================
# LISTS GO HERE


# ==================================================
# MAIN PROGRAM STARTS HERE
# execute program if exit code has not been received and there are tickets left
while name != "xxx" and ticket_count < MAX_TICKETS:

    # check that number of tickets has not been exceeded
    check_tickets(ticket_count, MAX_TICKETS)

    # GET DETAILS
    # get name, cannot be blank
    name = not_blank("Name:")
    print()

    if name == "xxx":
        continue

    ticket_price = get_ticket_price()

    if ticket_price == "invalid ticket price":
        continue

    ticket_count += 1
    ticket_sales += ticket_price
    print()

# ==================================================
# DATAFRAME PRINTS HERE
    name = name.title()
    all_names.append(name)
    all_tickets.append(ticket_price)

movie_frame = pandas.DataFrame(movie_data_dict)
print(movie_frame)
print()

# ==================================================
# POST MAIN PROGRAM GOES HERE
ticket_profit = ticket_sales - (5 * ticket_count)
print("Ticket Profit: ${:.2f}".format(ticket_profit))

if ticket_count == MAX_TICKETS:
    print("You have sold all the available tickets!")
else:
    print("You have sold {} tickets. \n"
          "There are {} places still available"
          .format(ticket_count, MAX_TICKETS - ticket_count))
