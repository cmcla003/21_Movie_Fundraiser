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

# *** Main Routine ***

# Set up dictionaries and lists to hold data.

# Ask user if they have used the program before and show instructions if needed

# Loop to get ticket details

    # Get name (can't be blank)
    name = not_blank("Name: ")

    # Get age (between 12 and 130)

    # Calculate ticket price

    # Loop to ask for snacks

    # Calculate snack price

    # Ask for payment method (apply surcharge if applicable)

# Calculate total sales & profit

# Output data to text file