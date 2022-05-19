# IMPORTS GO HERE
import pandas

# ==================================================
# FUNCTIONS GO HERE


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


def string_check(choice, options):
    is_valid = ""
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

# ==================================================
# VARIABLES
name = ""
ticket_count = 0
ticket_profit = 0
MAX_TICKETS = 5
ticket_sales = 0

snack_sales = 0

SURCHARGE = 5
surcharge_sales = 0
surcharge_profit = 0

# ==================================================
# DATAFRAME SHENANIGANS
# initialise lists
all_names = []
all_tickets = []
all_snacks = []
all_surcharge = []

# dataframe dictionary
movie_data_dict = {
    'Name': all_names,
    'Ticket': all_tickets,
    'Snacks': all_snacks,
    'Surcharge': all_surcharge
}

# ==================================================
# LISTS GO HERE
# snack options for user to choose from
valid_snacks = [
    ["popcorn", "p", "corn", "a"],
    ["M&M's", "m&m's", "mms", "m", "b"],
    ["pita chips", "chips", "pc", "pita", "c"],
    ["orange juice", "orange j" "o juice", "oj", "d"],
    ["water", "w", "e"]
]

# valid options for yes/no questions
yes_no = [
    ["yes", "y"],
    ["no", "n"]
]

# payment options for payment checker
payment_types = [
    ["card"],
    ["cash"]
]


# ==================================================
# MAIN PROGRAM STARTS HERE
# get details
# ask user for name as long as there are tickets remaining
while name != "xxx" and ticket_count < MAX_TICKETS:
    total_snack_cost = 0
    total_ticket_cost = 0
    if ticket_count < MAX_TICKETS - 1:
        print("=====================================")
        print("You have {} seats "
              "left".format(MAX_TICKETS - ticket_count))

    # warns user that there is only one seat left
    else:
        print("*** There is only ONE seat left! ***")

    # get name, cannot be blank
    name = not_blank("Name:").title()

# ==================================================
    # continue program if name is not exit code
    if name == "Xxx":
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
    total_ticket_cost += ticket_price

# ==================================================
    print()

    # ask user if they want a snack
    check_snack = "invalid choice"
    while check_snack == "invalid choice":
        want_snack = input("Do you want Snacks?").lower()
        check_snack = string_check(want_snack, yes_no)

    # snack list for snack checker
    snack_order = []
    if check_snack == "Yes":
        desired_snack = ""

        print("Snack options include:")
        print("A. Popcorn")
        print("B. M&M's")
        print("C. Pita Chips")
        print("D. Orange Juice")
        print("E. Water")
        print()

        while desired_snack != "xxx":

            desired_snack = input("Snack: ").lower()

            if desired_snack == "xxx":
                break

            snack_choice = string_check(desired_snack, valid_snacks)
            print("Snack Choice: ", snack_choice)
            print()

            if snack_choice != "xxx" and snack_choice != "invalid choice":
                snack_order.append(snack_choice)
                snack_price = 0

            if desired_snack in valid_snacks[0]:
                snack_price = 2.50

            elif desired_snack in valid_snacks[1]:
                snack_price = 3.00

            elif desired_snack in valid_snacks[2]:
                snack_price = 4.50

            elif desired_snack in valid_snacks[3]:
                snack_price = 4.50

            elif desired_snack in valid_snacks[4]:
                snack_price = 2.00

            snack_sales = snack_sales + snack_price
            total_snack_cost = total_snack_cost + snack_price

    print()
    if len(snack_order) == 0:
        print("Snacks Ordered: None")

    else:
        print("Snacks Ordered: ")

        for item in snack_order:
            print(item)

# ==================================================
    print()
    check_payment = "invalid choice"
    while check_payment == "invalid choice":
        print("What is your payment method?")
        payment_choice = input("Cash or Card?").lower()

        check_payment = string_check(payment_choice, payment_types)
        print("Payment Choice: ", (check_payment))
        print()

    print("Cost of Ticket: {:.2f}".format(total_ticket_cost))
    print("Cost of Snacks: {:.2f}".format(total_snack_cost))

    total_cost = total_snack_cost + total_ticket_cost

    # determine which payment option the user chose
    if payment_choice == "cash":
        print("Cost of Total Order: {:.2f}".format(total_cost))

    elif payment_choice == "card":
        total_cost_surcharge = total_cost + ((total_cost / 100) * SURCHARGE)
        surcharge_sales = (total_cost / 100) * SURCHARGE
        surcharge_profit = surcharge_profit + surcharge_sales
        print("Cost of Total Order, with Surcharge: {:.2f}".format(total_cost_surcharge))

# ==================================================
    # add user details to dataframe
    all_names.append(name)
    all_tickets.append(ticket_price)
    all_snacks.append(total_snack_cost)
    all_surcharge.append(surcharge_sales)

print()
# calculate profit from tickets
ticket_profit = ticket_sales - (5 * ticket_count)
print("Ticket Profit: {:.2f}".format(ticket_profit))

# calculate profit from snacks
snack_profit = (snack_sales / 10) * 2
print("Snack Profit: {:.2f}".format(snack_profit))

# calculate profit from surcharge
print("Surcharge Profit: {:.2f}".format(surcharge_profit))

print()
# PRINT DETAILS
movie_frame = pandas.DataFrame(movie_data_dict)
print(movie_frame)

# tell the user of any unsold tickets
print()
if ticket_count == MAX_TICKETS:
    print("You have sold all the available tickets!")
else:
    print("You have sold {} tickets. \n"
          "There are {} places still available"
          .format(ticket_count, MAX_TICKETS - ticket_count))
