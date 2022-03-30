# functions go here
def not_blank(question):
    valid = False

    while not valid:
        response = input(question)

        if response != "":
            return response
        else:
            print("Sorry, this cannot be blank")


def int_check(question, low_num, high_num):

    error = "Please enter a whole number between {} " \
            "and {}".format(low_num, high_num)

    valid = False
    while not valid:

        # ask user for age and check if is valid
        try:
            response = int(input(question))

            if response < low_num or response > high_num:
                print(error)
            else:
                return response

        # if an integer is not entered, display an error message
        except ValueError:
            print(error)


# variables go here
name = ""
count = 0
MAX_TICKETS = 5

# get details
while name != "xxx" and count < MAX_TICKETS:
    if count < 4:
        print("You have {} seats "
              "left".format(MAX_TICKETS - count))

    # warns user that there is only one seat left
    else:
        print("*** There is only ONE seat left! ***")

    # get name, cannot be blank
    name = not_blank("Name:")

    if name == "xxx":
        break

    count += 1

    # get age, between 12 and 130
    age = int_check("Age:", 12, 130)
    print()


if count == MAX_TICKETS:
    print("You have sold all the available tickets!")
else:
    print("You have sold {} tickets. \n"
          "There are {} places still available"
          .format(count, MAX_TICKETS - count))
