# IMPORTS GO HERE
import pandas

# initialise snack lists

all_names = ["Short", "Long", "Sheet", "Stuffed", "Dumpling"]

popcorn = []
mms = []
pita_chips = []
orange_juice = []
water = []

snack_lists = [popcorn, mms, pita_chips, orange_juice, water]

movie_data_dict = {
    'Name': all_names,
    'Popcorn': popcorn,
    'M&Ms': mms,
    'Pita Chips': pita_chips,
    'Orange Juice': orange_juice,
    'Water': water
}

test_data = [
    [[2, 'Popcorn'], [1, 'Pita Chips'], [1, 'Orange Juice']],
    [[]],
    [[1, 'Water']],
    [[1, 'Pita Chips'], [1, 'Orange Juice']],
    [[1, 'M&Ms'], [1, 'Pita Chips'], [3, 'Orange Juice']],
]

# ==================================================
# LISTS GO HERE
# snack options for user to choose from
valid_snacks = [
    ["popcorn", "p", "corn", "a"],
    ["M&M's", "m&m's", "mms", "m", "b"],
    ["pita chips", "chips", "pc", "pita", "c"],
    ["orange juice", "orange j" "o juice", "oj", "d"],
    ["water", "w", "e"]
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
print("Orange juice: ", snack_lists[3])
print("Water: ", snack_lists[4])

movie_frame = pandas.DataFrame(movie_data_dict)
movie_frame = movie_frame.set_index('Name')
print(movie_frame)
