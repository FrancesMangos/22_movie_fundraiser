import re


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


def get_snack():

    number_regex = "^[1-9]"

    # valid snacks holds list of all snacks
    # each item in valid snacks is a list with,
    # valid options for each snack - full name, letter code,
    # and any possible abbreviations

    valid_snacks = [
        ["popcorn", "p", "corn", "a"],
        ["M&Ms", "MMs", "m&ms", "mms", "m", "b"],
        ["pita chips", "chips", "pc", "pita", "c"],
        ["orange juice", "orange j" "o juice", "oj", "d"],
        ["water", "w", "e"]
    ]

    # holds snack order for single user
    snack_order = []

    desired_snack = ""
    while desired_snack != "xxx":
        total_amount = 0

        snack_row = []

        desired_snack = input("Snack: ").lower()

        if desired_snack == "xxx":
            return snack_order

        if re.match(number_regex, desired_snack):
            amount = int(desired_snack[0])
            desired_snack = desired_snack[1:]
            total_amount = total_amount + amount

        else:
            amount = 1
            desired_snack = desired_snack
            total_amount = total_amount + amount

        desired_snack = desired_snack.strip()

        snack_choice = string_check(desired_snack, valid_snacks)

        snack_row.append(amount)
        snack_row.append(snack_choice)

        # create a sum of the amount for each choice
        if snack_choice != "xxx" and snack_choice != "invalid choice":
            print("Snack Choice: {} {}".format(amount, snack_choice))
            print()
            snack_order.append(snack_row)

        else:
            print("Sorry - What you entered is invalid!")
            print()
# valid options for yes/no questions
yes_no = [
    ["yes", "y"],
    ["no", "n"]
]

# holds snack order for a single user
snack_order = []

# ask user if they want a snack
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
