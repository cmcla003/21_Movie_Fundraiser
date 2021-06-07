# valid snacks hols list of all snacks
# each item in valid snacks with valid options for each snack, incl abbreviations
valid_snacks = [
    ["popcorn", "p", "corn", "a"],
    ["M&M's", "m&m's", "mms", "m", "b"],
    ["pita chips", "chips", "pc", "pita", "c"],
    ["water","w", "d"]
]

# initalise variables
snack_ok=""
snack =""

# loop for testin purposes
for item in range (0,3):
    desired_snack = input("Snack: ").lower()

    # if snack in list return the full name
    for var_list in valid_snacks:

        # get full snack and format title case
        if desired_snack in var_list:
            snack = var_list[0].title()
            snack_ok = "yes"
            break

        else:
            snack_ok = "no"

    # if snack not valid ask question again
    if snack_ok == "yes":
        print("Snack Choice: ", snack)

    else:
        print("Invalid Choice")
