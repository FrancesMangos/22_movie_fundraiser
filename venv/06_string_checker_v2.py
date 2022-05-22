def string_check(choice, options):

    for var_list in options:
        is_valid = ""

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
    ["water", "w", "d"]
]

for item in range(0, 6):

    desired_snack = input("Snack: ").lower()

    snack_choice = string_check(desired_snack, valid_snacks)
    print("Snack Choice: ", snack_choice)
