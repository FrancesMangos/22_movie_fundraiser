# functions go here
def not_blank(question, error_message):
    valid = False

    while not valid:
        response = input(question)

        # checks if name is blank
        if response != "":
            return response
        # prints error message if name is blank
        else:
            print(error_message)

name = ""
count = 0
MAX_TICKETS = 5

while name != "xxx" and count < MAX_TICKETS:
    name = input("Name:")
    count += 1
