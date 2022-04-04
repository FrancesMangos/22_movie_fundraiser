# functions go here
def int_check(question):

    error = "Please enter a whole number more than 0"

    valid = False
    while not valid:

        # ask user for age and check if is valid
        try:
            response = int(input(question))

            if response <= 0:
                print(error)
            else:
                return response

        # if an integer is not entered, display an error message
        except ValueError:
            print(error)

# main program goes here
age = int_check("Age:")
