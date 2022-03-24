import random

name = input("What is your name?").title()
age = int(input("How old are you?"))

print("So you're {} and are {} years old?".format(name, age))

money = int(input("How much money do you have?"))
print("I'm gonna yoink 30% of your money from you!")

taken = (money / 10) * 3
money = money - taken

print("I took {:.2f} so now you have: {:.2f}".format(taken, money))
