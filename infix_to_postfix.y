%{
#include <stdio.h>
#include <stdlib.h>
%}

%token IDENTIFIER
%token PLUS MINUS MULTIPLY DIVIDE LPAREN RPAREN

%%

expression : expression PLUS term      { printf("%c ", $1); printf("%c ", $3); printf("+ "); }
           | expression MINUS term     { printf("%c ", $1); printf("%c ", $3); printf("- "); }
           | term                     { printf("%c ", $1); }
           ;

term       : term MULTIPLY factor     { printf("%c ", $1); printf("%c ", $3); printf("* "); }
           | term DIVIDE factor       { printf("%c ", $1); printf("%c ", $3); printf("/ "); }
           | factor                   { printf("%c ", $1); }
           ;

factor     : IDENTIFIER               { printf("%c ", $1); }
           | LPAREN expression RPAREN { printf("( "); printf("%c ", $2); printf(") "); }
           ;

%%

int main() {
    yyparse();
    printf("\n");
    return 0;
}

void yyerror(char *s) {
    printf("Error: %s\n", s);
    exit(1);
}
