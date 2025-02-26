# Functions
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

    print('''
    \nThe instructions have been printed
    ''')


# Main
instructions = check_string("Do you want to see the instructions? ")

if instructions == "yes":
    instruct()

print("\nProgram continues")
