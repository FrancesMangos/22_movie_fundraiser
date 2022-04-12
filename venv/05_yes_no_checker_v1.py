def yes_no(question):

    error = "Please answer will either yes/no"

    valid = False
    while not valid:


        response = input(question).lower()

        if response == "yes" or response == "y":
            valid = True
            return "yes"

        elif response == "no" or response == "n":
            valid = True
            return "no"

        else:
            print(error)

for item in range(0,6):
    want_snacks = yes_no("Does thou want any of thy snacks?")
