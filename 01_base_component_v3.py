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



# ********* Main Routine ********

# Set up dictionaries and lists to hold data.

# Ask user if they have used the program before and show instructions if needed

# intialise variables
MAX_TICKETS = 5

name = ""
ticket_count = 0
ticket_sales = 0

# initialuse lists
all_names = []
all_tickets = []

# Data frame dictionary
movie_data_dict = {
    'Name': all_names,
    'Ticket': all_tickets
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

    # get payment method (adds surcharge if needed)


# end of tickets/snacks/payment loop

# print details
movie_frame = pandas.DataFrame(movie_data_dict)
print(movie_frame)


 # Calculate ticket price & profit
ticket_profit = (ticket_sales - (5 * ticket_count))
print("Ticket Profit: ${:.2f}".format(ticket_profit))

if ticket_count == MAX_TICKETS:
    print("You have sold all available tickets.")
else:
    print("You have sold {} tickets. \n"
          "There are {} tickets available.".format(ticket_count, MAX_TICKETS-ticket_count))


    # Loop to ask for snacks

    # Calculate snack price

    # Ask for payment method (apply surcharge if applicable)

# Calculate total sales & profit

# Output data to text file