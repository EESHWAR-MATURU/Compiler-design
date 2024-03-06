%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
%}

%option noyywrap

%%
[0-9]+          { yylval = atoi(yytext); return 'NUMBER'; }
[a-zA-Z]+       { yylval = strdup(yytext); return 'ID'; }
[-+*/%()]       { return *yytext; }
[ \t\n]         ; // ignore whitespace

.               { fprintf(stderr, "invalid character\n"); }

%%

int main() {
    yylex();
    return 0;
}
