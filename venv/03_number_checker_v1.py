# functions go here
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

# main program goes here
age = int_check("Age:", 12, 130)
