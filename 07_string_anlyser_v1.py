import re

# works out wether string has numbers & seperates into amount and item

test_strings = [
    "Popcorn", "2 pc", "1.5 OJ", "4 OJ"
]

for item in test_strings:

    # regular expression to find if item starts with number
    number_regex ="^[1-9]"

    if re.match(number_regex, item):
        amount = int(item[0])
        desired_snack = item[1:]

    else:
        amount = 1
        desired_snack = item

    # remove white spaces around snack
    desired_snack = desired_snack.strip()

    # if item does not have number in front, set to 1

    # print order
    print("Amount: ", amount)
    print("Snack: ", desired_snack)
    print("Length of snack: ",len(desired_snack))