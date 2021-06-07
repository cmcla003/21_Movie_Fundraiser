# Function goes here
def yes_no(question):
    valid = False
    while not valid:
        # Ask user if they have played before
        response = input(question).lower().strip()

        # If  yes, output 'program continues'
        if response == "yes" or response == "y":
            response = "yes"
            return response

        # If no output 'display instructions'
        elif response == "no" or response == "n":
            response= "no"
            return response

        else:
            print("Please enter yes or no")

# Main routine goes here ...
for item in range(0,6):
    want_snacks = yes_no("Do you want snacks? ")
    print( "Answer OK. You chose {}".format(want_snacks))
    print()