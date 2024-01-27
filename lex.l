%{
#include <stdio.h>
%}

%%
bool|int|float   { printf("Keyword: %s\n", yytext); }
[-+]?[0-9]+     { printf("Constants: %s\n", yytext); }
[,.'"]+         { printf("Punctuation Chars: %s\n", yytext); }
[!@#$%^&*()]+   { printf("Special Chars: %s\n", yytext); }
[a-zA-Z]+       { printf("Identifiers: %s\n", yytext); }
[<>=]+       { printf("comparision: %s\n", yytext); }
%%
int yywrap() {
    // Returning 1 indicates the end of input
    return 1;
}

int main() {
    yylex();
    return 0;
}