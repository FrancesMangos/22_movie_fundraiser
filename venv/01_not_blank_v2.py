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

# main program goes here
name = not_blank("Name:",
                 "Sorry, this cannot be blank, please enter your name.")
