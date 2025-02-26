# Functions
def not_blank(question):
    """checks that a user has not left a response blank"""

    while True:
        response = input(question)

        if response != "":
            return response

        print("You cannot leave this blank, Please enter a response\n")


def num_check(question, datatype=int):
    """ Function to make sure user inputs an integer / float that is above 0 """

    # get correct error message for data type
    if datatype == int:
        err = "Please enter an integer above 0"
    else:
        err = "Please enter a number above 0"

    while True:

        # tests for exit code
        test_exit = input(question).lower()

        if test_exit == "xxx" or test_exit == "x":
            return "exit"

        # try statement for checking that it is of the correct datatype
        try:
            response = datatype(test_exit)

            if response > 0:
                return response
            else:
                print(err)

        except ValueError:
            print(err)


# Main
while 1:
    product_name = not_blank("Product Name: ")
    quantity_made = num_check("Quantity being made ")
    print(f"You are making {quantity_made} {product_name}\n")
    
