# Lab 2.3 - Operator Frequency Counter
OPERATORS = ['+', '-', '*', '/', '(', ')']

def count_operators(expression: str) -> dict[str, int]:
    """Return the count of each operator in the expression."""
    counts = {op: 0 for op in OPERATORS}

    for character in expression:
        if character in counts:
            counts[character] += 1
    return counts

if __name__ == "__main__":
    expression = input("Enter an arithmetic expression: ")
    result = count_operators(expression)
    print(f"Operator counts: {result}")
