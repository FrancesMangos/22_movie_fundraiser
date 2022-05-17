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
all_ages = []
all_tickets = []
all_snacks = []
all_payment_type = []
all_surcharge = []
all_total = []

popcorn = []
mms = []
pita_chips = []
orange_juice = []
water = []

snack_lists = [popcorn, mms, pita_chips, orange_juice, water]

# dataframe dictionary
movie_data_dict = {
    'Name': all_names,
    'Ticket': all_tickets,
    'Snacks': all_snacks,
    'Surcharge': all_surcharge,
    'Total Cost': all_total,
    'Popcorn': popcorn,
    'M&Ms': mms,
    'Pita Chips': pita_chips,
    'Orange Juice': orange_juice,
    'Water': water
}

# prices for each snack
price_dict = {
    'Popcorn': 2.5,
    'M&Ms': 3,
    'Pita Chips': 4.5,
    'Orange Juice': 3.25,
    'Water': 2
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
        snack_order = input("Snack: ")

    else:
        snack_order = []

    for item in snack_lists:
        item.append(0)

    for item in snack_order:
        if len(item) > 0:
            to_find = (item[1])
            amount = (item[0])
            add_list = movie_data_dict[to_find]
            add_list[-1] = amount

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
        total_cost = total_cost + ((total_cost / 100) * SURCHARGE)
        surcharge_sales = (total_cost / 100) * SURCHARGE
        surcharge_profit = surcharge_profit + surcharge_sales
        print("Cost of Total Order, with Surcharge: {:.2f}".format(total_cost))

# ==================================================
    # add user details to dataframe
    all_names.append(name)
    all_ages.append(age)
    all_tickets.append(ticket_price)
    all_snacks.append(total_snack_cost)
    all_payment_type.append(payment_choice)
    all_surcharge.append(surcharge_profit)
    all_total.append(total_cost)

print()
# PRINT DETAILS
movie_frame = pandas.DataFrame(movie_data_dict)
movie_frame = movie_frame.set_index('Name')

movie_frame["Sub Total"] = \
    movie_frame['Ticket'] + \
    movie_frame['Popcorn']*price_dict['Popcorn'] + \
    movie_frame['M&Ms']*price_dict['M&Ms'] + \
    movie_frame['Pita Chips']*price_dict['Pita Chips'] + \
    movie_frame['Orange Juice']*price_dict['Orange Juice'] + \
    movie_frame['Water']*price_dict['Water']

movie_frame = movie_frame.rename(columns={'Orange Juice': 'OJ',
                                      'Pita Chips': 'Chips'}, inplace = True)
print(movie_frame)

# ==================================================
print()
# calculate profit from tickets
ticket_profit = ticket_sales - (5 * ticket_count)
print("Ticket Profit: {:.2f}".format(ticket_profit))

# calculate profit from snacks
snack_profit = (snack_sales / 10) * 2
print("Snack Profit: {:.2f}".format(snack_profit))

# calculate profit from surcharge
print("Surcharge Profit: {:.2f}".format(surcharge_profit))

# ==================================================
# tell the user of any unsold tickets
print()
if ticket_count == MAX_TICKETS:
    print("You have sold all the available tickets!")
else:
    print("You have sold {} tickets. \n"
          "There are {} places still available"
          .format(ticket_count, MAX_TICKETS - ticket_count))
