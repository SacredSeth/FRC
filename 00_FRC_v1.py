# Functions
import pandas
from tabulate import tabulate
from datetime import date


def make_statement(statement, decoration=""):
    """Decorates headings with chosen decoration"""

    return f"{decoration * 3} {statement} {decoration * 3}"


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


def instruct():
    """Prints instructions"""

    print(make_statement("Instructions", "ℹ️"))

    print('''This program will ask you for... 
        - The name of the product you are selling 
        - How many items you plan on selling 
        - The costs for each component of the product 
          (variable expenses)
        - Whether or not you have fixed expenses (if you have 
          fixed expenses, it will ask you what they are).
        - How much money you want to make (ie: your profit goal)

    It will also ask you how much the recommended sales price should 
    be rounded to.

    The program outputs an itemised list of the variable and fixed 
    expenses (which includes the subtotals for these expenses). 

    Finally it will tell you how much you should sell each item for 
    to reach your profit goal. 

    The data will also be written to a text file which has the 
    same name as your product and today's date.

        ''')


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

# initialise variables

# assume we have no fixed responses for now
fixed_subtotal = 0
fixed_panda_string = ""

# print heading
print(make_statement("Fund Raising Calculator", "💰"))

# ask for instructions
want_instructions = check_string("\nDo you want to see the instructions? ")
if want_instructions == "yes":
    instruct()

print()

# get product details
product_name = not_blank("Product name: ")
quantity_made = num_check("Quantity being made: ")

# get variable expenses
print("\nGetting Variable Costs")
variable_expenses = get_expenses("variable", quantity_made)

variable_panda = variable_expenses[0]
variable_subtotal = variable_expenses[1]
print()

# ask user if they have fixed expenses and retrieve them
has_fixed = check_string("Do you have fixed expenses? ")
if has_fixed == "yes":
    fixed_expenses = get_expenses("fixed")

    fixed_panda_string = fixed_expenses[0]
    fixed_subtotal = fixed_expenses[1]

    # if the user doesn't enter fixed expenses
    # set the panda to be empty with "" so it doesn't display
    if fixed_subtotal == 0:
        has_fixed = "no"
        fixed_panda_string = ""

total_expenses = variable_subtotal + fixed_subtotal
total_expenses_string = f"Total Expenses: ${total_expenses:.2f}"

# Get profit goal

# string / output area

# **** get current date for heading and filename ****
today = date.today()

# get day, month

