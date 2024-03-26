%{
#include "y.tab.h"
%}

%%

"+"     { return PLUS; }
"-"     { return MINUS; }
"*"     { return MULTIPLY; }
"/"     { return DIVIDE; }
"("     { return LPAREN; }
")"     { return RPAREN; }
[0-9]+  { yylval.num = atoi(yytext); return NUMBER; }
[a-zA-Z]+ { yylval.id = yytext[0]; return IDENTIFIER; }
[ \t\n]  ; /* skip whitespace */
.       { return yytext[0]; } /* return any other character as is */

%%

int yywrap() {
    return 1;
}
