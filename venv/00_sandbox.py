valid_snacks = [
    ["popcorn", "p", "corn", "a"],
    ["M&M's", "m&m's", "mms", "m", "b"],
    ["pita chips", "chips", "pc", "pita", "c"],
    ["orange juice", "orange j" "o juice", "oj", "d"],
    ["water", "w", "e"]
]

variable_one = input("Snack: ")
if variable_one == valid_snacks[0]:
    print("Snack: {}".format(valid_snacks[0][0]))
