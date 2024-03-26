%{
#include <stdio.h>
#include <stdlib.h>
%}

%token NUMBER IDENTIFIER
%token PLUS MINUS MULTIPLY DIVIDE LPAREN RPAREN
%left PLUS MINUS
%left MULTIPLY DIVIDE

%%

expression : expression PLUS expression   { $$ = $1 + $3; }
           | expression MINUS expression  { $$ = $1 - $3; }
           | expression MULTIPLY expression { $$ = $1 * $3; }
           | expression DIVIDE expression { $$ = $1 / $3; }
           | LPAREN expression RPAREN     { $$ = $2; }
           | NUMBER                      { $$ = $1; }
           | IDENTIFIER                  { $$ = $1; }
           ;

%%

int main() {
    yyparse();
    return 0;
}

void yyerror(char *s) {
    printf("Error: %s\n", s);
    exit(1);
}
