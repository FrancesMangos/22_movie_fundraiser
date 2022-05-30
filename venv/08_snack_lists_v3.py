import pandas

# initialise snack lists

all_names = ["Short", "Long", "Sheet", "Stuffed", "Dumpling"]

popcorn = []
mms = []
pita_chips = []
orange_juice = []
water = []

snack_lists = [popcorn, mms, pita_chips, orange_juice, water]

# dataframe dictionary
movie_data_dict = {
    'Name': all_names,
    'Popcorn': popcorn,
    'M&Ms': mms,
    'Pita Chips': pita_chips,
    'Orange Juice': orange_juice,
    'Water': water,
}

price_dict = {
    'Popcorn': 2.5,
    'Water': 2,
    'Pita Chips': 4.5,
    'M&Ms': 3,
    'Orange Juice': 3.25,
}

# test data
test_data = [
    [[2, 'Popcorn'], [1, 'Pita Chips'], [1, 'Orange Juice']],
    [[]],
    [[1, 'Water']],
    [[1, 'Popcorn'], [1, 'Orange Juice']],
    [[1, 'M&Ms'], [1, 'Pita Chips'], [3, 'Orange Juice']]
]

count = 0
for client_order in test_data:

    for item in snack_lists:
        item.append(0)

    snack_order = test_data[count]
    count += 1

    for item in snack_order:
        if len(item) > 0:
            to_find = (item[1])
            amount = (item[0])
            add_list = movie_data_dict[to_find]
            add_list[-1] = amount

print()
print("Names: ", all_names)
print("Popcorn: ", snack_lists[0])
print("M&Ms: ", snack_lists[1])
print("Pita Chips: ", snack_lists[2])
print("Orange Juice: ", snack_lists[3])
print("Water: ", snack_lists[4])

movie_frame = pandas.DataFrame(movie_data_dict)
movie_frame = movie_frame.set_index('Name')

movie_frame["Sub Total"] = \
    movie_frame['Ticket'] + \
    movie_frame['Popcorn']*price_dict['Popcorn'] + \
    movie_frame['M&Ms']*price_dict['M&Ms'] + \
    movie_frame['Pita Chips']*price_dict['Pita Chips'] + \
    movie_frame['Orange Juice']*price_dict['Orange Juice'] + \
    movie_frame['Water']*price_dict['Water']

movie_frame = movie_frame.rename(columns={'Orange Juice': 'OJ',
                                           'Pita Chips': 'Chips'})

print(movie_frame)
