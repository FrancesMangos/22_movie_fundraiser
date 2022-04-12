# functions go here
def not_blank(question):
    valid = False

    while not valid:
        response = input(question)

        if response != "":
            return response
        else:
            print("Sorry, this cannot be blank")


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


# variables go here
name = ""
ticket_count = 0
ticket_sales = 0
MAX_TICKETS = 5

# get details
while name != "xxx" and ticket_count < MAX_TICKETS:
    if ticket_count < MAX_TICKETS - 1:
        print("You have {} seats "
              "left".format(MAX_TICKETS - ticket_count))

    # warns user that there is only one seat left
    else:
        print("*** There is only ONE seat left! ***")

    # get name, cannot be blank
    name = not_blank("Name:")

    # continue program if name is not exit code
    if name == "xxx":
        break

    # get age, between 12 and 130
    age = int_check("Age:")

    # check if age is valid
    if age < 12:
        print("Sorry you are too young for this movie!")
        continue
    elif age > 130:
        print("That is very old, it looks like a mistake!")
        continue

    # determine ticket price based on age
    if age < 16:
        ticket_price = 7.5

    elif age < 65:
        ticket_price = 10.5

    else:
        ticket_price = 6.5


    ticket_count += 1
    ticket_sales += ticket_price

print()
# calculate ticket price
ticket_profit = ticket_sales - (5 * ticket_count)
print("Ticket Profit: {:.2f}".format(ticket_profit))

# tell the user of any unsold tickets
if ticket_count == MAX_TICKETS:
    print("You have sold all the available tickets!")
else:
    print("You have sold {} tickets. \n"
          "There are {} places still available"
          .format(ticket_count, MAX_TICKETS - ticket_count))
