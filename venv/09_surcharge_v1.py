# imports go here


# functions go here
def string_check(choice, options):

    is_valid = ""
    chosen = ""

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


# main program goes here
payment_method = [
    ["cash", "ca"],
    ["card", "cr"]
]

name = ""
while name != "Xxx":
    name = input("Name: ").title()
    print()
    if name == "Xxx":
        break

    how_pay = "invalid choice"
    while how_pay == "invalid choice":
        how_pay = input("Please choose a payment method - cash/card")
        how_pay = string_check(how_pay, payment_method)

        if how_pay not in payment_method:
            print("Sorry - Please choose cash/card!")
        print()

    subtotal = float(input("Sub Total? $"))

    if how_pay == "Credit":
        surcharge = 0.05 * subtotal
    else:
        surcharge = 0

    total = subtotal + surcharge

    print("Name: {} | Subtotal: ${} | Surcharge: ${:.2f}"
          " | Total Payable: ${}".format(name, subtotal, surcharge, total))
