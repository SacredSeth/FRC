# Functions
def make_statement(statement, decoration=""):
    """Decorates headings with chosen decoration"""

    return f"{decoration * 3} {statement} {decoration * 3}"


# Main
print(make_statement("Product A", "$"))
