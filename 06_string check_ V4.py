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
        return "invalid choice"


# valid snacks holds list of all snacks
# each item in valid snacks with valid options for each snack, incl abbreviations
valid_snacks = [
    ["popcorn", "p", "corn", "a"],
    ["M&M's", "m&m's", "mms", "m", "b"],
    ["pita chips", "chips", "pc", "pita", "c"],
    ["water","w", "d"]
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

        desired_snack = input("Snack: ").lower().strip()
        if desired_snack == "xxx":
            break

        # check is snack is valid
        snack_choice = string_check(desired_snack, valid_snacks)
        print("Snack Choice: ", snack_choice)

        # add snack to list
        if snack_choice != "xxx" and snack_choice != "invalid choice":
            snack_order.append(snack_choice)

# show snack order
print()
if len(snack_order) == 0:
    print("Snacks Ordered: None")

else:
    print("Snacks Ordered: ")
    for item in snack_order:
        print(item)