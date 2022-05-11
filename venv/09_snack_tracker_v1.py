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

# valid snacks holds list of all snacks
# each item in valid snacks is a list with,
# valid options for each snack - full name, letter code,
# and any possible abbreviations
valid_snacks = [
    ["popcorn", "p", "corn", "a"],
    ["M&M's", "m&m's", "mms", "m", "b"],
    ["pita chips", "chips", "pc", "pita", "c"],
    ["water", "w", "d"]
]

# valid options for yes/no questions
yes_no = [
    ["yes", "y"],
    ["no", "n"]
]
snack_order = []

# ask user if they want a snack
check_snack = "invalid choice"
while check_snack == "invalid choice":
    want_snack = input("Do you want Snacks?").lower()
    check_snack = string_check(want_snack, yes_no)

if check_snack == "Yes":
    desired_snack = ""

    while desired_snack != "xxx":

        num_snacks, desired_snack = input("Snack: ").split()
        desired_snack = desired_snack.lower()

        if desired_snack == "xxx":
            break

        snack_choice = string_check(desired_snack, valid_snacks)

        print("Number of {} is {}".format(snack_choice, num_snacks))

        if snack_choice != "xxx" and snack_choice != "invalid choice":
            snack_order.append(snack_choice)


print()
if len(snack_order) == 0:
    print("Snacks Ordered: None")

else:
    print("Snacks Ordered: ")

    for item in snack_order:
        print(item)
