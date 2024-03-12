class RecursiveDescentParser:
    def __init__(self, input_string):
        self.input_string = input_string
        self.current_token = None
        self.index = 0

    def next_token(self):
        if self.index < len(self.input_string):
            self.current_token = self.input_string[self.index]
            self.index += 1
        else:
            self.current_token = None

    def match(self, expected_token):
        if self.current_token == expected_token:
            self.next_token()
        else:
            raise SyntaxError(f"Expected {expected_token}, found {self.current_token}")

    def parse_E(self):
        self.parse_T()
        self.parse_E_prime()

    def parse_E_prime(self):
        if self.current_token == '+':
            self.match('+')
            self.parse_T()
            self.parse_E_prime()
        elif self.current_token == '$':
            pass  # Epsilon transition
        else:
            raise SyntaxError("Invalid token in E_prime")

    def parse_T(self):
        self.parse_F()
        self.parse_T_prime()

    def parse_T_prime(self):
        if self.current_token == '*':
            self.match('*')
            self.parse_F()
            self.parse_T_prime()
        elif self.current_token == '$':
            pass  # Epsilon transition
        else:
            raise SyntaxError("Invalid token in T_prime")

    def parse_F(self):
        if self.current_token == '(':
            self.match('(')
            self.parse_E()
            self.match(')')
        elif self.current_token == 'a':
            self.match('a')
        else:
            raise SyntaxError("Invalid token in F")

    def parse_S(self):
        self.match('a')
        self.parse_A()
        self.match('c')
        self.parse_B()

    def parse_A(self):
        if self.current_token == 'd':
            self.match('d')
            self.match('b')
        elif self.current_token == 'x':
            self.match('x')
        else:
            raise SyntaxError("Invalid token in A")


    def parse_B(self):
        if self.current_token == 'a':
            self.match('a')
            self.parse_B()
        elif self.current_token == 'x':
            self.match('x')
            self.parse_S()
        elif self.current_token == 'b':
            self.match('b')
        else:
            raise SyntaxError("Invalid token in B")


if __name__ == "__main__":
    parser = RecursiveDescentParser("aaxcb")
    parser.next_token()  # Initialize current_token
    try:
        parser.parse_S()
        print("Parsing successful")
    except SyntaxError as e:
        print("Parsing error:", e)
