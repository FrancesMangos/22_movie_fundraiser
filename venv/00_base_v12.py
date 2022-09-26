# This program is called: Movie Fundraiser.
# My name is: France Magno.
# I started this project on: 21st of March 2022.
# This program asks for, and stores, the names, food and drink preferences, -
# - payment options, and total cost of orders for people who are buying tickets to the movie.

# ==================================================
# IMPORTS GO HERE
import re
import pandas

# ==================================================
# FUNCTIONS GO HERE


# This function makes sure that inputs that go through questions, that requires an input to not be blank, to force -
# - users who do enter a blank input to answer the question again until they answer with a not blank input.
def not_blank(question):
    valid = False

    while not valid:
        response = input(question)

        # This checks if name is blank. If it is blank it will print an error message, and will keep -
        # - asking the question until they enter an input that is not blank. If it is not blank, it will continue.
        if response != "":
            return response
        else:
            print("Sorry - This cannot be blank!")
            print()


# This function makes sure that inputs that go through questions, that requires -
# - an input to be an integer, to keep answering the question until they answer with a valid integer.
def int_check(question):

    error = "Sorry - Please enter a whole number more than 0"

    valid = False
    while not valid:

        # This asks the user for their age. If the user's age is not an integer, it will print an error message and -
        #  - the program will keep asking the question until the user enters a valid integer.
        try:
            response = int(input(question))

            # This checks that the user's age is not a negative number
            if response <= 0:
                print(error)
            else:
                return response

        except ValueError:
            print(error)

    print()


# This function keeps track of how many tickets are sold, and if they ever exceed the amount of tickets that are -
# - actually available, after which they will alert the user how many tickets have been sold and how many seats are left.
def check_tickets(tickets_sold, ticket_limit):
    # This checks if the amount of tickets sold is less that the amount of tickets available. If the -
    # - latter is more than the former, the program will print a message displaying how many seats are left.
    if tickets_sold < ticket_limit - 1:
        print("You have {} seats "
              "left".format(ticket_limit - tickets_sold))

    else:
        print("*** There is only ONE seat left! ***")

    return ""


# This function determines the ticket price for the user depending on their age.
def get_ticket_price():
    age = int_check("Age:")
    print()

    # This checks if the user is old enough for the movie. If they are too -
    # - young the program will tell them that they are too young, and restarts the program.
    if age < 12:
        print("Sorry - You are too young for this movie.")
        print()
        return "invalid ticket price"

    # This checks if the user's input is realistic. If the user's age exceeds the most realistic oldest age for a -
    # - person, the program will tell them they must have entered their age wrong, and restarts the program.
    if age > 130:
        print("Sorry - Your input is too big, it looks like a mistake")
        print()
        return "invalid ticket price"

    # The next following lines of code determines the price of the user's ticket depending on their age.
    if age < 16:
        price_of_ticket = 7.5

    elif age < 65:
        price_of_ticket = 10.5

    else:
        price_of_ticket = 6.5

    return price_of_ticket


# This function makes sure that inputs for a question, that has a set amount of valid inputs that go through it, is -
# - one of the valid inputs. The program will keep asking the user the question until their enter one of the valid inputs.
def string_check(choice, options):

    is_valid = ""
    chosen = ""

    for var_list in options:

        # This checks if the user's input is one of the available inputs.
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


# This function asks the user for their desired snack and drink preferences. The program -
# - lets users buy more than one of the same snack or drink, but never more than a certain amount. The program also -
# - allows users to buy multiple varieties of snacks and drinks.
def get_snack():

    number_regex = "^[1-9]"

    # This list holds the list of available snacks. It holds the full name, -
    # - shortenings and any other possible abbreviations for that snack
    valid_snacks = [
        ["popcorn", "p", "pop", "corn", "a"],
        ["M&Ms", "MMs", "m&ms", "mms", "m", "b"],
        ["pita chips", "chips", "pc", "pita", "c"],
        ["orange juice", "orange j" "o juice", "oj", "d"],
        ["water", "w", "h20", "e"]
    ]
    # This prints out the instructions. It tells the user how to order, and -
    # - the limitations with their order. This also tells the user how to finish with their order.
    print("----- Snack Options -----")
    print("A. Popcorn")
    print("B. M&Ms")
    print("C. Pita Chips")
    print("D. Orange Juice")
    print("E. Water")
    print()
    print("- Enter number then the snack, ex: 3popcorn or 3pop.")
    print("- Maximum of Four for a Snack!")
    print("- Slight variations for a snack name will be accepted")
    print()
    print("To exit, simply type 'xxx' when it asks for a snack")
    print()

    # This holds the snacks and drinks a single user orders.
    snack_order = []

    desired_snack = ""
    # This checks if the user has finished their order, initiated by entering the exit code.
    while desired_snack != "xxx" or desired_snack != "n":

        # This temporarily holds the snacks and drinks of a single user's order. This is because we can take -
        # - or add things to this temporary list before permanently adding it to the first list.
        snack_row = []

        desired_snack = input("Snack: ").lower()

        if desired_snack == "xxx":
            return snack_order

        # This checks if the user's input has a number before the snack choice, indicating that they want more than one.
        if re.match(number_regex, desired_snack):
            amount = int(desired_snack[0])
            desired_snack = desired_snack[1:]

        else:
            amount = 1
            desired_snack = desired_snack

        desired_snack = desired_snack.strip()

        snack_choice = string_check(desired_snack, valid_snacks)

        # This checks if the user has ordered less that the limited amount of one snack or drink -
        # - they can order. If the user does exceed this number the input they provided is cancel.
        if amount >= 5:
            print("Sorry - Only 4 maximum of the same snack!")
            snack_choice = "invalid choice"
            amount = ""

        snack_row.append(amount)
        snack_row.append(snack_choice)

        if snack_choice != "xxx" and snack_choice != "invalid choice":

            print("Snack Choice: {} {}".format(amount, snack_choice))
            snack_order.append(snack_row)

        print()
    print()


# This function formats the currency entered into the question to replicate how money would be shown in real life.
def currency(x):
    return "${:.2f}".format(x)


# This functions shows the user the instructions on how to use this program.
def instructions(options):
    show_instructions = False
    while not show_instructions:
        show_help = input("Would you like to see the instructions?").lower()
        if show_help == "yes" or show_help == "y":
            print("The program will ask you for your:")
            print("Age, Any Snacks you would like to purchase, and your preferred Payment Method")
            print("---")
            print("You must enter a valid option or response for each question")
            print("To exit, simply type 'xxx' once the program asks for a name.")
            print()
            return show_help
        elif show_help == "no" or show_help == "n":
            print("You did not want to see the instructions")
            print()
            return show_help
        else:
            print("Sorry - Please enter yes or no")
            print()

# ==================================================
# VARIABLES GO HERE
# This variable monitors how many tickets can be sold.
MAX_TICKETS = 100

# This variable holds the user's name during their session.
name = ""

# These variables monitor the amount of tickets sold.
ticket_count = 0
ticket_sales = 0

# ==================================================
# DATAFRAME STUFF GOES HERE
# This variable holds the list to every name that has been passed through the program.
all_names = []
# This variable holds the list to the ticket price associated with each user that has used the program.
all_tickets = []

# These variables hold lists to the amount of a particular -
# - snack or drink each user has or has not ordered during their session.
popcorn = []
mms = []
pita_chips = []
orange_juice = []
water = []

snack_lists = [popcorn, mms, pita_chips, orange_juice, water]

surcharge_mult_list = []

# This variable holds the list to the headings used in the -
# - summary later in the program that prints out all user details.
summary_headings = ["Popcorn", "M&Ms", "Pita Chips", "Orange Juice",
                    "Water", "Snack Profit", "Ticket Profit", "Surcharge Profit",
                     "Total Profit"]

summary_data = []

# This variable holds the dictionary to the details of users who use the program. This consists of the user's -
# -  name, ticket price, snack and drink preferences, and the surcharge multiplier if a user has paid with a card.
movie_data_dict = {
    'Name': all_names,
    'Ticket': all_tickets,
    'Popcorn': popcorn,
    'M&Ms': mms,
    'Pita Chips': pita_chips,
    'Orange Juice': orange_juice,
    'Water': water,
    'Surcharge_Multiplier': surcharge_mult_list
}

# This variable holds the dictionary to each snack and drink, and the corresponding price to each one.
price_dict = {
    'Popcorn': 2.5,
    'M&Ms': 3,
    'Pita Chips': 4.5,
    'Orange Juice': 3.25,
    'Water': 2,
}

# This variable stores the profit from each profitable variable, such as the ticket price, and snack and drink prices.
summary_data_dict = {
    'Item': summary_headings,
    'Amount': summary_data
}

# ==================================================
# LISTS GO HERE
# This variable holds the valid options for yes/no questions.
yes_no = [
    ["yes", "y"],
    ["no", "n"]
]

# This variable holds the order of a user's preferred snacks and drinks.
snack_order = []

# This variable holds the valid options for the card/cash checker.
payment_method = [
    ["cash", "ca"],
    ["credit", "card", "cr"]
]

# ==================================================
# MAIN PROGRAM STARTS HERE
print("Program Launches...")
print()

# This checks if the user has not yet inputted the exit code, nor has exceeded the amount of tickets available to be sold.
while name != "xxx" and ticket_count < MAX_TICKETS:

    check_tickets(ticket_count, MAX_TICKETS)
    print()

# ==================================================
    # GET DETAILS
    # ASK USER FOR NAME
    # This calls the not_blank function to ensure that the user's input cannot be blank.
    name = not_blank("Name:")
    print()

    # This checks if the user has inputted the exit code. If they -
    # -  have they bypass all the questions, and are brought to the end of the program.
    if name == "xxx":
        continue

# ==================================================
    # ASK USER IF THEY WANT INSTRUCTIONS
    instructions(yes_no)
    print()

# ==================================================
    # ASK USER FOR AGE
    # This calls the get_ticket_price function which asks the user -
    # - or their age, then determines the price of the user depending on their age.
    ticket_price = get_ticket_price()

    # This checks if the user's input is invalid. If it is the user is brought back to the beginning of the program.
    if ticket_price == "invalid ticket price":
        continue

    ticket_count += 1
    ticket_sales += ticket_price

    # This puts both the name, and ticket price of the user into their corresponding lists.
    name = name.title()
    all_names.append(name)
    all_tickets.append(ticket_price)

# ==================================================
    # ASK USER FOR SNACKS
    snack_order = get_snack()

    for item in snack_lists:
        item.append(0)

    # This checks if the user wants more than one of a particular -
    # - snack or drink. If they do, the program adds as much of the snack or drink as requested as the user.
    for item in snack_order:
        if len(item) > 0:
            to_find = (item[1])
            amount = (item[0])
            add_list = movie_data_dict[to_find]
            add_list[-1] = amount

    print()
# ==================================================
    # ASK FOR PAYMENT METHOD + SURCHARGE
    how_pay = "invalid choice"

    while how_pay == "invalid choice":
        how_pay = input("Please choose a payment method - cash/credit").strip().lower()
        how_pay = string_check(how_pay, payment_method)

    print()

    # This determines if the user will be charged extra if they use a card to pay.
    if how_pay == "Credit":
        surcharge_multiplier = 0.05
    else:
        surcharge_multiplier = 0

    # This puts the surcharge multiplier (which can be 0) in its corresponding list.
    surcharge_mult_list.append(surcharge_multiplier)

# ==================================================
# DATAFRAME PRINTS HERE - PART 1

movie_frame = pandas.DataFrame(movie_data_dict)
movie_frame = movie_frame.set_index('Name')

movie_frame["Snacks"] = \
    movie_frame['Popcorn'] * price_dict['Popcorn'] + \
    movie_frame['M&Ms'] * price_dict['M&Ms'] + \
    movie_frame['Pita Chips'] * price_dict['Pita Chips'] + \
    movie_frame['Orange Juice'] * price_dict['Orange Juice'] + \
    movie_frame['Water'] * price_dict['Water']

movie_frame["Sub Total"] = \
    movie_frame['Ticket'] + \
    movie_frame['Snacks']

movie_frame['Surcharge'] = \
    movie_frame['Sub Total'] * movie_frame['Surcharge_Multiplier']

movie_frame['Total'] = movie_frame['Sub Total'] + \
    movie_frame['Surcharge']

# This renames the longer headings in the dataframe to shorter abbreviations.
movie_frame = movie_frame.rename(columns={'Orange Juice': 'OJ',
                                          'Pita Chips': 'Chips',
                                          'Surcharge_Multiplier': 'SM'})

# ==================================================
# PROFIT CALCULATIONS HERE
# This calculates the profit from snacks and drinks.
for item in snack_lists:
    summary_data.append(sum(item))

snack_total = movie_frame['Snacks'].sum()
snack_profit = snack_total * 0.2

# This calculates the profit from tickets.
ticket_profit = ticket_sales - (5 * ticket_count)
total_profit = snack_profit + ticket_profit

# This calculates the profit from surcharge.
surcharge_profit = movie_frame['Surcharge'].sum()
surcharge_profit = surcharge_profit

# This adds all the profit from the other profitable variables into the total profit.
total_profit = total_profit + surcharge_profit

# This puts all the profit variables in the dictionary.
dollar_amounts = [snack_profit, ticket_profit, surcharge_profit, total_profit]
for item in dollar_amounts:
    item = "${:.2f}".format(item)
    summary_data.append(item)

# ==================================================
# DATAFRAME PRINTS HERE - PART 2
summary_frame = pandas.DataFrame(summary_data_dict)
summary_frame = summary_frame.set_index('Item')

# This ensures that there is no limit to the amount of columns that can be printed.
pandas.set_option('display.max_columns', None)

# This calls the currency function that makes all the profit variables are formatted in a way that mimics real life.
add_dollars = ['Ticket', 'Snacks', 'Surcharge', 'Total', 'Sub Total']
for item in add_dollars:
    movie_frame[item] = movie_frame[item].apply(currency)

movie_frame.to_csv('ticket_details.csv')
summary_frame.to_csv('snack_summary.csv')

# This prints the summary of details, snacks and drinks.
print()
print("----- Ticket / Snack Information -----")
print("Note: for full details please visit excel file called Movie Fundraiser")
print()
print(movie_frame[['Ticket', 'Snacks', 'Sub Total', 'Surcharge', 'Total']])

# This prints the summary of profits.
print()
print("----- Profit / Snack Summary -----")
print()
print(summary_frame)

# ==================================================
# POST MAIN PROGRAM/TICKET COUNT GOES HERE
print()
if ticket_count == MAX_TICKETS:
    print("You have sold all the available tickets!")
else:
    print("You have sold {} tickets. \n"
          "There are {} places still available"
          .format(ticket_count, MAX_TICKETS - ticket_count))
