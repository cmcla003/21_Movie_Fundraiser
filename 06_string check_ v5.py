import re


# Function goes here
def string_check(choice, options):

    for var_list in options:

        is_valid = ""
        chosen = ""

        # if snack is in one of the lists , return full snack
        if choice in var_list:

            # get full snack and format
            chosen = var_list[0].title()
            is_valid = "yes"
            break

        else:
            is_valid = "no"

    if is_valid == "yes":
        return chosen

    else:
        print("Please enter a valid option")
        print()
        return "invalid choice"

# regular expression to find if item starts with number
number_regex ="^[1-9]"

# valid snacks holds list of all snacks
# each item in valid snacks with valid options for each snack, incl abbreviations
valid_snacks = [
    ["popcorn", "p", "corn", "a"],
    ["M&M's", "m&m's", "mms", "m","mm", "MM", "b"],
    ["pita chips", "chips", "pc", "pita", "c"],
    ["water","w", "d"],
    ["orange", "orange juice", "OJ", "oj","e"]
]

yes_no =[
    ["yes","y"],["no","n"]
]

# holds snack order for a single user
snack_order =[]

check_snack = "invalid choice"
while check_snack == "invalid choice":
    want_snack = input("Do you want to order snacks? ").lower().strip()
    check_snack = string_check(want_snack,yes_no)

if check_snack == "Yes":

    desired_snack= ""
    while desired_snack != "xxx":
        # ask for snack convert to lowercase
        desired_snack = input("Snack: ").lower()
        if desired_snack == "xxx":
            break

        #If item has number seperate into two (number/string)
        if re.match(number_regex, desired_snack):
            amount = int(desired_snack[0])
            desired_snack = desired_snack[1:]
        else:
            amount = 1
            desired_snack=desired_snack
        # remove white space
        desired_snack = desired_snack.strip()

        # check is snack is valid
        snack_choice = string_check(desired_snack, valid_snacks)

        # check snack amount is valid
        if amount >=5:
            print("Sorry, we have a four snack maximum")
            snack_choice ="invalid choice"

        # add snack and amount to list
        amount_snack = "{} {}".format(amount, snack_choice)

        # add snack to list
        if snack_choice != "xxx" and snack_choice != "invalid choice":
            snack_order.append(amount_snack)

# show snack order
print()
if len(snack_order) == 0:
    print("Snacks Ordered: None")

else:
    print("Snacks Ordered: ")
    for item in snack_order:
        print(item)