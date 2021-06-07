# mak functon more lfeixble to asses yes no and check string response

# Function goes here
def string_checker(question, to_check):
    valid = False
    while not valid:
        # Ask user if they have played before
        response = input(question).lower().strip()

        # If  yes, output 'program continues'
        if response in to_check:
            return response

        else:
            for item in to_check:
                # check reposne isthe first letter of item in list
                if response in item[0]:
                    # return entire response nit just first letter
                    return item

        print("Sorry that is not a valid response")

# Main routine goes here ...
for item in range(0,6):
    want_snacks = string_checker("Do you want snacks?", ["yes", "no"])
    print( "Answer OK. You chose {}".format(want_snacks))
    print()