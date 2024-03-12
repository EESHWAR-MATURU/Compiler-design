def parse(grammar, input_string):
    # Parse the grammar rules
    rules = {}
    for line in grammar.split('\n'):
        if line.strip():
            lhs, rhs = line.split()
            rules[lhs] = rhs
    # Initialize the stack with the start symbol
    stack = ['S']
    # Process the input string
    for char in input_string:
        top = stack[-1]
        if top in rules:
            # Replace the non-terminal with its production
            production = rules[top]
            stack.pop()
            stack.extend(reversed(production))
        elif top == char:
            # Match the terminal symbol
            stack.pop()
        else:
            return "NO"  # Invalid input
    # Check if the stack is empty (successful parsing)
    return "YES" if not stack else "NO"
if __name__ == "__main__":
    print("Enter the grammar rules (one rule per line, format: lhs rhs):")
    grammar_rules = input()
    input_str = input("Enter the input string: ")
    result = parse(grammar_rules, input_str)
    print("Result:", result)
