from collections import defaultdict 

class CFGParser:
    def __init__(self) -> None:
        self.num_variables = int(input("Enter the number of non-terminals: "))
        self.variables = input("Enter the non-terminals: ").split()
        self.productions = defaultdict(list)

        for i in range(self.num_variables):
            self.productions[self.variables[i]] = []
            num_productions = int(input(f"Enter the number of productions for {self.variables[i]}: "))
            for j in range(num_productions):
                self.productions[self.variables[i]].append(input("Enter the RHS of production: "))
    
    def to_string(self):
        print(self.num_variables)
        print(self.variables)
        for var in self.productions:
            print(var, end=" -> ")
            print(*self.productions[var], sep=" | ")
            print()

    def check_left_rec(self):
        for i in range(self.num_variables):
            for prod in self.productions[self.variables[i]]:
                if self.variables[i] == prod[0]:
                    print("Left recursion")
                    print(self.variables[i] + " -> " + prod)
    
    def left_factoring(self):
        for i in range(self.num_variables):
            recursions = []
            terminals = []
            for prod in self.productions[self.variables[i]]:
                if prod.islower():
                    terminals.append(prod)
                if self.variables[i] == prod[0]:
                    recursions.append(prod)
            if len(recursions) == 0:
                continue
            else:
                arr1 = []
                arr2 = []
                if len(terminals) > 0:
                    for term in terminals:
                        arr1.append(term + self.variables[i] + "'")
                else:
                    arr1.append(self.variables[i] + "'")
                for rec in recursions:
                    arr2.append(rec[1:] + self.variables[i] + "'")
                arr2.append("E")
                self.productions[self.variables[i]] = arr1
                self.productions[self.variables[i] + "'"] = arr2


if __name__ == "__main__":
    parser = CFGParser()
    parser.to_string()
    parser.check_left_rec()
    parser.left_factoring()
    parser.to_string()
