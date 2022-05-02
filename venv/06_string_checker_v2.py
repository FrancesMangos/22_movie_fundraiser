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

# variables
snack_ok = ""
snack = ""

# loop three times to make testing quicker
for item in range(0, 3):
    desired_snack = input("Snack: ").lower()

    for var_list in valid_snacks:

        if desired_snack in var_list:

            snack = var_list[0].title()
            snack_ok = "yes"
            break

        else:
            snack_ok = "no"

    if snack_ok == "yes":
        print("Snack Choice: ", snack)

    else:
        print("Invalid Choice")

