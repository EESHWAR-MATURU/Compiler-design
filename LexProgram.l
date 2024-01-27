%{
#include<stdio.h>
int kwc=0,idc=0;
%}
kw "int"|"float"|"char"|"double"|"case"|"switch"|"if"|"else"
%%
{kw} {printf("%s is keyword", yytext); kwc++;}
[a-zA-Z][a-zA-Z0-9]* {printf("%s is an identifier",yytext);idc++;}
. {}
%%

int yywrap()
{
return 1;
}

main()
{
printf("enter the string ");
yylex();
printf("Number of keywords=%d",kwc);
printf("Number of identifers =%d",idc);
}