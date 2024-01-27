def remove_left_recursion(non_terminals, productions):
    modified_productions = []

    for non_terminal in non_terminals:
        alpha = []
        beta = []

        for production in productions[non_terminal]:
            if production[0] == non_terminal:
                alpha.append(production[1:])
            else:
                beta.append(production)

        if alpha:
            new_non_terminal = non_terminal + "'"
            modified_productions.append([non_terminal, new_non_terminal])
            modified_productions.append([new_non_terminal] + alpha + [new_non_terminal, '|', 'ε'])
            modified_productions.extend([new_non_terminal] + b for b in beta + [['ε']])
        else:
            modified_productions.append([non_terminal] + b for b in beta)

    return modified_productions

def main():
    # Step 1: Read CFG
    num_non_terminals = int(input("Enter number of non-terminals: "))
    non_terminals = input("Enter the non-terminals, with the start variable as the first one: ").split()

    productions = {}

    for non_terminal in non_terminals:
        num_productions = int(input(f"Give number of productions for {non_terminal}: "))
        production_list = []

        for _ in range(num_productions):
            rhs = input(f"Give right-hand side of Production for {non_terminal}: ").split()
            production_list.append(rhs)

        productions[non_terminal] = production_list

    print("\nOriginal Productions:")
    for non_terminal in productions:
        for production in productions[non_terminal]:
            print(f"{non_terminal} -> {' '.join(production)}")

    # Step 2: Identify immediate left recursion
    left_recursion_detected = False
    for non_terminal in non_terminals:
        for production in productions[non_terminal]:
            if production[0] == non_terminal:
                left_recursion_detected = True
                break
        if left_recursion_detected:
            break

    if left_recursion_detected:
        # Step 3: If left recursion exists, do left factoring and removal
        modified_productions = remove_left_recursion(non_terminals, productions)

        print("\nProductions after removing immediate left recursion:")
        for production in modified_productions:
            print(' '.join(production))
    else:
        print("\nNo left recursion detected. Original productions remain unchanged.")

if __name__ == "__main__":
    main()
