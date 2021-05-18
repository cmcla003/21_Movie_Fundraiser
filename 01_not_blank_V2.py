# function goes here

def not_blank(question, error):
    valid = False

    while not valid:
        response = input(question)

        while response != "":
            return response
        else:
            print(error)


# main routine goes here
name = not_blank("Name: ", "This can't be blank please enter your name" )



