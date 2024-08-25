import sys

input = sys.stdin.read().strip()

def minimize_expression(expression):
    terms = expression.split('-')
    total = 0

    for i, term in enumerate(terms):
        sum_in_term = sum(map(int, term.split('+')))
        if i == 0:
            total += sum_in_term
        else:
            total -= sum_in_term

    return total

print(minimize_expression(input))
