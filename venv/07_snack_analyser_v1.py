import re

test_strings = [
    "Popcorn",
    "2 pc",
    "1.5OJ",
    "4OJ"
]

for item in test_strings:

    number_regex = "^[1-9]"

    if re.match(number_regex, item):
        amount = int(item[0])
        desired_snack = item[1:]

    else:
        amount = 1
        desired_snack = item

    desired_snack = desired_snack.strip()

    print("Amount: ", amount)
    print("Snack: ", desired_snack)
    print("Length of Snack: ", len(desired_snack))

