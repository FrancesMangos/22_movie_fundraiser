def string_checker(question, to_check):

    valid = False
    while not valid:

        response = input(question).lower()

        if response in to_check:
            return response

        else:
            for item in to_check:

                if response == item[0]:

                    return item

        print("Sorry! That is not a valid response!")
