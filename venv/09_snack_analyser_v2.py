import re


def string_check(choice, options):

    chosen = ""
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

valid_snacks = [
    ["popcorn", "p", "corn", "a"],
    ["M&M's", "m&m's", "mms", "m", "b"],
    ["pita chips", "chips", "pc", "pita", "c"],
    ["orange juice", "o", "oj", "d"],
    ["water", "w", "e"]
]

# valid options for yes/no questions
yes_no = [
    ["yes", "y"],
    ["no", "n"]
]

snack_order = []

number_regex = "^[1-9]"

check_snack = "invalid choice"
while check_snack == "invalid choice":
    want_snack = input("Do you want Snacks?").lower()
    check_snack = string_check(want_snack, yes_no)

if check_snack == "Yes":

    desired_snack = ""
    while desired_snack != "xxx":

        desired_snack = input("Snack: ").lower()

        if desired_snack == "xxx":
            break

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
            snack_choice = "invalid choice"

        amount_snack = "{} {}".format(amount, snack_choice)
        print("Snack: {}".format(amount_snack))
        print()

        if snack_choice != "xxx" and snack_choice != "invalid choice":
            snack_order.append(amount_snack)

print()
if len(snack_order) == 0:
    print("Snacks Ordered: None")

else:
    print("Snacks Ordered: ")

    for item in snack_order:
        print(item)

