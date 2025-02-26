# Functions
def check_string(question):
    """Checks user answers yes or no"""

    while True:

        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Please answer yes or no")


# Main
likes_tea = check_string("Do you like tea? ")

if likes_tea == "yes":
    print("\nWelcome to tea drinking society")
else:
    print("\nGet out of here non believer")
