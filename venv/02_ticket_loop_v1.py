name = ""
count = 0
MAX_TICKETS = 5

# execute program if exit code has not been received and there are tickets left
while name != "xxx" and count < MAX_TICKETS:
    name = input("Name:")
    count += 1
