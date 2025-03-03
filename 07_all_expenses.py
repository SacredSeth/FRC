# Functions
import pandas
from tabulate import tabulate


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
        response = input(question).lower()

        if response == exit_code or response == exit_code[0]:
            return ""

        # try statement for checking that it is of the correct datatype
        try:
            response = datatype(response)

            if response > 0:
                return response
            else:
                print(err)

        except ValueError:
            print(err)


def get_expenses(exp_type, quantity=1):
    """gets variable / fixed expenses and outputs
    panda (as a string) and a subtotal of the expenses"""

    # Lists for panda
    items_list = []
    amounts_list = []
    ppi_list = []

    # Expenses dict
    expenses_dict = {
        "Item": items_list,
        "Amount": amounts_list,
        "$ / Item": ppi_list
    }

    # default amount to 1 for fixed expenses and
    # to avoid PEP 8 error for variable expenses
    amount = quantity

    # Loop to get expenses
    while 1:

        # get item name
        item_name = not_blank("Item Name: ")

        # check user enter at lease one variable expense
        if (exp_type == "variable" and item_name == "xxx") and len(items_list) == 0:
            print("Oops - You need to have at least one product.")
            continue

        elif item_name == "xxx":
            break

        if exp_type == "variable":

            # get item amount <enter> defaults to number of products being made
            amount = num_check(f"Product Quantity <enter for {quantity}>: ", int, "")

            if amount == "":
                amount = quantity

        cost_per = num_check("Price for one? $", float)

        items_list.append(item_name)
        amounts_list.append(amount)
        ppi_list.append(cost_per)

    # make panda
    expense_frame = pandas.DataFrame(expenses_dict)

    # calculate cost
    expense_frame['Cost'] = expense_frame['Amount'] * expense_frame['$ / Item']

    # calculate subtotal
    subtotal = expense_frame['Cost'].sum()

    # Apply currency formatting
    add_dollars = ['Amount', '$ / Item', 'Cost']
    for var in add_dollars:
        expense_frame[var] = expense_frame[var].apply(currency)

    # make expense frame into a string with the desired columns
    if exp_type == "variable":
        expense_string = tabulate(expense_frame, headers='keys', tablefmt='psql', showindex=False)
    else:
        expense_string = tabulate(expense_frame[['Item', 'Cost']], headers='keys', tablefmt='psql', showindex=False)

    # return all items for now so we can check loop
    return expense_string, subtotal


def currency(x):
    """Formats numbers as currency ($x.xx)"""
    return f"${x:.2f}"


# Main

quantity_made = num_check("Quantity being made: ")

print("\nGetting Variable Costs")
variable_expenses = get_expenses("variable", quantity_made)
variable_panda = variable_expenses[0]
variable_subtotal = variable_expenses[1]
print()

print(variable_panda)
print(f"Variable subtotal: ${variable_subtotal:.2f}")

# print("Getting Fixed Costs")
# fixed_expenses = get_expenses("fixed")
# num_fixed = len(fixed_expenses)
# print(f"You entered {num_fixed} items")
