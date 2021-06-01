# start of loop

# intialise variables
name = ""
count = 0
MAX_TICKETS = 5

while name != "xxx" and count < MAX_TICKETS:
    # tells user how many tickets left
    if count < 4:
        print("You have {} places left".format(MAX_TICKETS-count))
    #  on place left
    else:
        print("***You have ONE place left***")

    # get details
    name = input("Name: ")
    count +=1

if count == MAX_TICKETS:
    print("You have sold all available tickets.")