# Prompt for the number of non-terminals
num_non_terminals = int(input("Enter number of non-terminals: "))

# Prompt for the non-terminals
non_terminals = input("Enter the non-terminals, with the start variable as the first one: ").split()

# Store productions in a dictionary
productions = {}
for non_terminal in non_terminals:
    num_productions = int(input(f"Give number of productions for {non_terminal}: "))
    productions[non_terminal] = []
    for i in range(1, num_productions + 1):
        production = input(f"Give right hand side of Production {i} for {non_terminal}: ")
        productions[non_terminal].append(production)
def has_immediate_left_recursion(productions, non_terminal):
    return any(production.startswith(non_terminal + " ") for production in productions[non_terminal])
def left_factor(productions, non_terminal):
    common_prefix = ""
    for production in productions[non_terminal]:
        if production.startswith(non_terminal + " "):
            common_prefix = common_prefix + production[1]
            production = production[len(common_prefix) + 1:]
        else:
            break

    if common_prefix:
        new_non_terminal = non_terminal + "'"
        productions[non_terminal] = [common_prefix + new_non_terminal] + [production for production in productions[non_terminal] if not production.startswith(non_terminal + " ")]
        productions[new_non_terminal] = [production[len(common_prefix):] for production in productions[non_terminal] if production.startswith(non_terminal + " ")]
def left_factor(productions, non_terminal):
    common_prefix = ""
    for production in productions[non_terminal]:
        if production.startswith(non_terminal + " "):
            common_prefix = common_prefix + production[1]
            production = production[len(common_prefix) + 1:]
        else:
            break

    if common_prefix:
        new_non_terminal = non_terminal + "'"
        productions[non_terminal] = [common_prefix + new_non_terminal] + [production for production in productions[non_terminal] if not production.startswith(non_terminal + " ")]
        productions[new_non_terminal] = [production[len(common_prefix):] for production in productions[non_terminal] if production.startswith(non_terminal + " ")]
def remove_left_recursion(productions):
    for non_terminal in non_terminals:
        if has_immediate_left_recursion(productions, non_terminal):
            left_factor(productions, non_terminal)

            # Replace direct left-recursive productions
            direct_left_recursive_productions = [production for production in productions[non_terminal] if production.startswith(non_terminal + " ")]
            for production in direct_left_recursive_productions:
                productions[non_terminal].remove(production)
                for other_production in productions[non_terminal]:
                    productions[non_terminal].append(other_production + production[len(non_terminal):])

            # Add ε-production if necessary
            if "" in productions[non_terminal]:
                productions[non_terminal].append(non_terminal + "'")
                productions[non_terminal].remove("")
# Print the modified productions
print("Modified productions:")
for non_terminal, productions in productions.items():
    print(non_terminal, productions)
