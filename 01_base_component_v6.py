# import statements
import re
import pandas


# functions go here

# checks ticket name is not blank
def not_blank(question):
    valid = False

    while not valid:
        response = input(question)

        # if response is not blank prgram continues
        while response != "":
            return response

        # If name is blank, show error and repeat the loop
        else:
            print("This can't be blank please enter a name")

# number check function
def int_check(question):
    error = "Please enter a whole number between 12 and 130 "

    valid = False
    while not valid:

        try:
            response = int(input(question))

            if response <=0:
                print(error)
            else:
                return response

        except ValueError:
            print(error)

# checks ticekts lett and warns user if max tickets being approached
def check_tickets(tickets_sold, ticket_limit):

    if tickets_sold < ticket_limit - 1:
        print("You have {} places left".format(ticket_limit - tickets_sold))
    #  on place left
    else:
        print("*** There is ONE seat left! ***")

    return ""

# get ticket price
def get_ticket_price():
    # Get age (between 12 and 130)
    age = int_check("Age: ")

    # check age of person
    if age <12:
        print("Sorry you are too young for this movie")
        return "invalid ticket price"
    elif age > 130:
        print("That is very old, it looks like a mistake.")
        return "invalid ticket price"

    # adjust ticekt price based on age
    if age < 16:
        ticket_price = 7.5
    elif age < 65:
        ticket_price = 10.5
    else:
        ticket_price = 6.5

    return ticket_price

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

# get snacks
def get_snack():

    # regular expression to find if item starts with number
    number_regex ="^[1-9]"

    # valid snacks holds list of all snacks
    # each item in valid snacks with valid options for each snack, incl abbreviations
    valid_snacks = [
        ["popcorn", "p", "corn", "a"],
        ["M&Ms", "m&ms", "mms", "m","mm", "MM", "b"],
        ["pita chips", "chips", "pc", "pita", "c"],
        ["water","w", "d"],
        ["Orange Juice", "orange juice", "OJ", "oj","e"]
    ]

    # holds snack order for a single user
    snack_order = []

    desired_snack = ""
    while desired_snack != "xxx":

        snack_row = []

        # ask for snack convert to lowercase
        desired_snack = input("Snack: ").lower()
        if desired_snack == "xxx":
            return snack_order

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
        if amount >= 5:
            print("Sorry, we have a four snack maximum")
            snack_choice = "invalid choice"

        # add snack and amount to list
        snack_row.append(amount)
        snack_row.append(snack_choice)

        # add snack to list
        if snack_choice != "xxx" and snack_choice != "invalid choice":
            snack_order.append(snack_row)

# ********* Main Routine ********

# Set up dictionaries and lists to hold data.

# Ask user if they have used the program before and show instructions if needed

# intialise variables
MAX_TICKETS = 5

name = ""
ticket_count = 0
ticket_sales = 0

# initialise lists
all_names = []
all_tickets = []
popcorn = []
mms = []
pita_chips = []
water = []
orange_juice = []

snack_lists = [popcorn, mms, pita_chips, water, orange_juice]

#list for valid yes/no response
yes_no =[
    ["yes","y"],["no","n"]
]

# list valid response for payment
pay_method = [
    ["cash", "ca"],
    ["credit", "cr"]
]

#store surcharge multiplier
surcharge_multi_list = []

# Data frame dictionary
movie_data_dict = {
    'Name': all_names,
    'Ticket': all_tickets,
    'Popcorn': popcorn,
    'Water': water,
    'Pita Chips': pita_chips,
    'M&Ms': mms,
    'Orange Juice': orange_juice,
    'Surcharge_Multiplier': surcharge_multi_list
}

# Price for snacks dictionary
price_dict = {
    'Popcorn': 2.5,
    'Water': 2,
    'Pita Chips': 4.5,
    'M&Ms': 3,
    'Orange Juice': 3.25
}
# ask user if used program before & show instructions

# Loop to get ticket details
while name != "xxx" and ticket_count < MAX_TICKETS:

    # check number of tickets has not been exceeded
    check_tickets(ticket_count, MAX_TICKETS)

    # *** get ticket details ***

    # get name can't "be blank
    name = not_blank("Name: ")

    # end loop if exit code entered
    if name == "xxx":
        break

    # get ticket price based on age
    ticket_price = get_ticket_price()

    # if age invalid, restart loop (get name again)
    if ticket_price == "invalid ticket price":
        continue

    ticket_count +=1
    ticket_sales += ticket_price

    # add names and ticekt price to lists
    all_names.append(name)
    all_tickets.append(ticket_price)

    # get snacks
    check_snack = "invalid choice"
    while check_snack == "invalid choice":
        want_snack = input("Do you want to order snacks? ").lower().strip()
        check_snack = string_check(want_snack, yes_no)

    if check_snack == "Yes":
        snack_order = get_snack()
    else:
        snack_order = []

    # assume snack purchased
    for item in snack_lists:
        item.append(0)

    for item in snack_order:
        if len(item)  > 0:
            to_find = (item[1])
            amount = (item[0])
            add_list = movie_data_dict[to_find]
            add_list[-1] = amount

    # get payment method (adds surcharge if needed)

    # Ask for payment method
    how_pay = "invalid choice"
    while how_pay == "invalid choice":
        how_pay = input("Please choose a payment method of cash or credit ").lower()
        how_pay = string_check(how_pay, pay_method)

    # calculate surcharge
    if how_pay == "Credit":
        surcharge_multiplier = 0.05
    else:
        surcharge_multiplier = 0

    surcharge_multi_list.append(surcharge_multiplier)
# end of tickets/snacks/payment loop

# print details
print()
movie_frame = pandas.DataFrame(movie_data_dict)
movie_frame = movie_frame.set_index('Name')

movie_frame["Snacks"] = \
    movie_frame['Popcorn'] * price_dict['Popcorn'] + \
    movie_frame['Water'] * price_dict['Water'] + \
    movie_frame['Pita Chips'] * price_dict['Pita Chips'] + \
    movie_frame['M&Ms'] * price_dict['M&Ms'] + \
    movie_frame['Orange Juice'] * price_dict['Orange Juice']

movie_frame["Sub Total"] = movie_frame['Ticket'] + movie_frame ['Snacks']

movie_frame["Surcharge"] = movie_frame["Sub Total"] * movie_frame["Surcharge_Multiplier"]

movie_frame["Total"] = movie_frame["Sub Total"] + movie_frame['Surcharge']

movie_frame = movie_frame.rename(columns={'Orange Juice': 'OJ', 'Pita chips': 'Chips',
                                          "Surcharge_Multiplier": 'SM'})

# set columns to be printed
pandas.set_option('display.max_columns', None)
# display to 2 dp
pandas.set_option('precision', 2)

print_all = input("Print all columns? enter y for yes ")
if print_all =="y":
    print(movie_frame)
else:
    print(movie_frame[['Ticket','Snacks', 'Sub Total', 'Surcharge', 'Total']])

print()

 # Calculate ticket price & profit
ticket_profit = (ticket_sales - (5 * ticket_count))
print("Ticket Profit: ${:.2f}".format(ticket_profit))

if ticket_count == MAX_TICKETS:
    print("You have sold all available tickets.")
else:
    print("You have sold {} tickets. \n"
          "There are {} tickets available.".format(ticket_count, MAX_TICKETS-ticket_count))


# Calculate total sales & profit

# Output data to text file