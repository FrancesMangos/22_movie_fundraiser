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


def string_check(choice, options):

    is_valid = ""
    chosen = ""

    for var_list in options:

        if choice in var_list:

            chosen = var_list[0].title()
            is_valid = "yes"
            break

        else:
            is_valid == "no"

    if is_valid == "yes":
        return chosen
    else:
        return "invalid choice"


def get_snack():

    number_regex = "^[1-9]"

    # valid snacks holds list of all snacks
    # each item in valid snacks is a list with,
    # valid options for each snack - full name, letter code,
    # and any possible abbreviations

    valid_snacks = [
        ["popcorn", "p", "corn", "a"],
        ["M&M's", "m&m's", "mms", "m", "b"],
        ["pita chips", "chips", "pc", "pita", "c"],
        ["orange juice", "orange j" "o juice", "oj", "d"],
        ["water", "w", "e"]
    ]

    # holds snack order for single user
    snack_order = []

    desired_snack = ""
    while desired_snack != "xxx":

        snack_row = []

        desired_snack = input("Snack: ").lower()

        if desired_snack == "xxx":
            return snack_order

        if re.match(number_regex, desired_snack):
            amount = int(desired_snack[0])
            desired_snack = desired_snack[1:]

        else:
            amount = 1
            desired_snack = desired_snack

        desired_snack = desired_snack.strip()

        snack_choice = string_check(desired_snack, valid_snacks)

        if amount >= 5:
            print("Sorry - Only 4 maximum of the same snack!")
            print()
            snack_choice = "invalid choice"
            amount = ""

        snack_row.append(amount)
        snack_row.append(snack_choice)

        if snack_choice != "xxx" and snack_choice != "invalid choice":

            print("Snack Choice: {} {}".format(amount, snack_choice))
            print()
            snack_order.append(snack_row)

        else:
            print("Sorry - What you entered is invalid!")
            print()


# ==================================================
# VARIABLES GO HERE


MAX_TICKETS = 5

name = ""

ticket_count = 0
ticket_sales = 0

# ==================================================
# DATAFRAME STUFF GOES HERE
# details
all_names = []
all_tickets = []

# movie data dictionary
movie_data_dict = {
    'Name': all_names,
    'Ticket': all_tickets
}

# ==================================================
# LISTS GO HERE
# valid options for yes/no questions
yes_no = [
    ["yes", "y"],
    ["no", "n"]
]

# holds snack order for a single user
snack_order = []

# valid options for cash/card checker
payment_method = [
    ["cash", "ca"],
    ["card", "cr"]
]

# ==================================================
# MAIN PROGRAM STARTS HERE
# execute program if exit code has not been received and there are tickets left
while name != "xxx" and ticket_count < MAX_TICKETS:

    # check that number of tickets has not been exceeded
    check_tickets(ticket_count, MAX_TICKETS)

# ==================================================
    # GET DETAILS
    # ASK USER FOR NAME
    # name cannot be blank
    name = not_blank("Name:")
    print()

    if name == "xxx":
        continue

# ==================================================
    # ASK USER FOR AGE
    # make sure age is within range
    # determine ticket price according to age
    ticket_price = get_ticket_price()

    if ticket_price == "invalid ticket price":
        continue

    ticket_count += 1
    ticket_sales += ticket_price
    print()

# ==================================================
    # ASK USER FOR SNACKS + YES/NO
    check_snack = "invalid choice"
    while check_snack == "invalid choice":
        want_snack = input("Do you want Snacks?").lower()
        check_snack = string_check(want_snack, yes_no)

    if check_snack == "Yes":
        print("Snack options include:")
        print("A. Popcorn")
        print("B. M&M's")
        print("C. Pita Chips")
        print("D. Orange Juice")
        print("E. Water")
        print()
        snack_order = get_snack()

    else:
        snack_order = []

    print()
    if len(snack_order) == 0:
        print("Snacks Ordered: None")

    else:
        print("Snacks Ordered: ")

        ''' for item in snack_order:
            print(item)
            '''

        print(snack_order)

# ==================================================
    # ASK FOR PAYMENT METHOD + SURCHARGE
    how_pay = "invalid choice"
    while how_pay == "invalid choice":
        how_pay = input("Please choose a payment method - cash/card")
        how_pay = string_check(how_pay, payment_method)

    if how_pay == "Credit":
        surcharge_multiplier = 0.05
    else:
        surcharge_multiplier = 0

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
