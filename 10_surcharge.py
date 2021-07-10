

# Function goes here
# WARNING response returned is Title Case

# string checker
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


# Main routing
pay_method = [
    ["cash", "ca"],
    ["credit", "cr"]
]
# ask user for name
name =""
while name != "xxx":
    name = input(("Name: "))
    if name == "xxx":
        break

    # Ask for payment method
    how_pay = "invalid choice"
    while how_pay == "invalid choice":
        how_pay = input("Please choose a payment method of cash or credit ").lower()
        how_pay = string_check(how_pay, pay_method)

    subtotal = float(input("Subtotal: $"))

    # calculate surcharge
    if how_pay == "Credit":
        surcharge = 0.05 * subtotal
    else:
        surcharge = 0

    # calculate total
    total = subtotal + surcharge

    print("Name: {} | Subtotal: ${:.2f} | Surcharge {:.2f} | Total: ${:.2f}".format(name, subtotal, surcharge, total))
