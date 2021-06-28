# Function goes here
def string_check(choice, options):

    for var_list in options:

        # if snack is in one of the lists , return full snack
        if choice in var_list:

            # get full snack and format
            chosen = var_list[0].title()
            is_valid = "yes"
            break

        else:
            is_valid = "no"
            continue

    if is_valid == "yes":
        return chosen
    else:
        return "Invalid Choice"


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

check_snack = "invalid choice"
while check_snack == "invalid choice":
    want_snack = input("Do you want to order snacks? ").lower()
    check_snack = string_check(want_snack,yes_no)

# loop for testing purposes
for item in range (0,6):
    desired_snack = input("Snack: ").lower()

    # check is snack is valid
    snack_choice = string_check(desired_snack, valid_snacks)
    print("Snack Choice: ", snack_choice)

