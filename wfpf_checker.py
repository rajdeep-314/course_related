# Well-formed propositional formula (WFPF) checker
# Suggested by the instructor during CS2020A - Discrete Mathematics

import string

# Conditions for an expression being a WFPF
# - Every propositional variable is a WFPF
# - Every propositional constant is a WFPF
# - If x is a WFPF, then ~x is also a WFPF
# - If x and y are WFPF's, then x^y, x_y, x->y and x<->y are all WFPF's
# - Nothing else is a WFPF

# Notation
# ~   :  negation
# ^   :  conjunction (AND)
# _   :  disjunction (OR)
# ->  :  conditional        [@ also works]
# <-> :  biconditional      [# also works]
# ()  :  parenthesis pair


# Validates the expression's parenthesis
# For example,
# (abcd(e)()f(())) is valid
# (abcd(e)( isn't
def paren_check(expression):
    stack = []
    for i in range(len(expression)):
        if expression[i] == '(':
            stack.append('(')
        elif expression[i] == ')':
            if stack[-1:] == ['(']:
                stack.pop()
            else:
                return False
    return not stack

# Checks if an expression without parenthesis is a WFPF
# Checks for all non-negation operators,
# then calls itself on what lies to the
# left and right of the operators and combines
# the results obtained.
# If no such operators are found, it should either
# be a single Latin character or a ~ followed by a
# single character.
# An expression like ~~x would thus be invalid
def check_without_paren(expression):
    for i in range(len(expression)):
        if expression[i] in '^_@#':
            return check_without_paren(expression[:i]) and check_without_paren(expression[i+1:])
    if len(expression) == 1:
        return expression in string.ascii_letters
    elif len(expression) == 2:
        return expression[0] == '~' and expression[1] in string.ascii_letters
    return False


# The main check function, called
# by the check_helper function
def check(expression):
    # Parenthesis validation
    if not paren_check(expression):
        return False

    # Removes all parenthesis from a
    # parenthesis-valid expression by
    # evaluating the expression inside
    # parenthesis-pairs. If this expression
    # is valid, it's replaced with an 'x',
    # otherwise with a '$', as they are valid
    # and invalid, respectively
    while '(' in expression:
        stack = []
        for i in range(len(expression)):
            if expression[i] == '(':
                stack.append((i, ')'))
            elif expression[i] == ')':
                if len(stack) == 1:
                    opening, closing = stack[0][0], i
                    break
                else:
                    stack.pop()
        replacement = ['$', 'x'][check(expression[opening+1:closing])]
        expression = expression[:opening] + replacement + expression[closing+1:]
    
    # The expression has been reduced
    # to a parenthesis-less equivalent
    # at this stage, which we check
    return check_without_paren(expression)


# Performs some basic pre-processing
# Replaces -> with @ and <-> with #
# for the sake of ease
# Also gets rid of all whitespaces
def check_helper(expression):
    return check(''.join(expression.replace('<->', '#').replace('->', '@').split()))


# The user can enter as many expresssions
# as they want. Not entering anything ends
# the otherwise infinite loop
while True:
    input_expr = input("Enter an expression : ")
    if input_expr:
        print(["Invalid", "Valid"][check_helper(input_expr)])
    else:
        break
