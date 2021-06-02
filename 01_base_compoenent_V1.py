# import statements

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
def int_check (question):
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

# *** Main Routine ***

# Set up dictionaries and lists to hold data.

# Ask user if they have used the program before and show instructions if needed

# Loop to get ticket details
# intialise variables
name = ""
count = 0
MAX_TICKETS = 5

while name != "xxx" and count < MAX_TICKETS:
    # tells user how many tickets left
    if count < 4:
        print("You have {} places left".format(MAX_TICKETS - count))
    #  on place left
    else:
        print("***You have ONE place left***")

    # Get name (can't be blank)
    name = not_blank("Name: ")

    if name == "xxx":
        break

    # Get age (between 12 and 130)
    age = int_check("Age: ")

    if age <12:
        print("Sorry you are too young for this movie")
        continue
    elif age > 130:
        print("That is very old, it looks like a mistake.")
        continue

    count += 1

if count == MAX_TICKETS:
    print("You have sold all available tickets.")
else:
    print("You have sold {} tickets. \n"
          "There are {} tickets available.".format(count, MAX_TICKETS-count))


    # Calculate ticket price

    # Loop to ask for snacks

    # Calculate snack price

    # Ask for payment method (apply surcharge if applicable)

# Calculate total sales & profit

# Output data to text file