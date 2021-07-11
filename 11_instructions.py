# functions go here

def string_check(choice, options):

    is_valid = ""
    chosen = ""

    for var_list in options:

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

def instructions(options):
    show_help = "invalid choice"

    while show_help == "invalid choice":
        show_help = input("Would you like to read the instructions? ").lower().strip()
        show_help = string_check(show_help,options)

    if show_help == "Yes":
        print()
        print("******* Movie Fundraiser Instructions *******")
        print()
        print("1. Enter your name and age to order tickets \n"
              "2. Enter the snacks you wish to purchase \n"
              "3. Enter your payment details (cash/credit) \n"
              "A summary will be printed to show your final order")

    return ""


# *** main routnine ***
# list for valid yes/no response
yes_no = [
    ["yes", "y"], ["no", "n"]
]

# ask if instructions needed
instructions(yes_no)
print()
print("Program continues ... ")