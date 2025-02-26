# Functions
def not_blank(question):
    """checks that a user has not left a response blank"""

    while True:
        response = input(question)

        if response != "":
            return response

        print("You cannot leave this blank, Please enter a response\n")


def num_check(question, datatype=int, exit_code="xxx"):
    """ Function to make sure user inputs an integer / float that is above 0 """

    # get correct error message for data type
    if datatype == int:
        err = "Please enter an integer above 0"
    else:
        err = "Please enter a number above 0"

    while True:

        # tests for exit code
        test_exit = input(question).lower()

        if test_exit == exit_code or test_exit == exit_code[0]:
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


def get_expenses(exp_type):
    """gets variable / fixed expenses and outputs
    panda (as a string) and a subtotal of the expenses"""

    # Lists for panda
    items_list = []

    # Expenses dict

    # Loop to get expenses
    while 1:
        item_name = not_blank("Item Name: ")

        # check user enter at lease one variable expense
        if (exp_type == "variable" and item_name == "xxx") and len(items_list) == 0:
            print("Oops - You have to have at least one product")


# Main
