%{
int charCount = 0;
int wordCount = 0;
int lineCount = 1;
int blankCount = 0;
char input_file[20];
%}

%%
[^\n ]+   { wordCount++; charCount += yyleng; }
[\n]          { lineCount++; charCount++; }
[ ]       { blankCount++; charCount++; }

%%
int yywrap()
{
    return 1;
}
int main() {
    printf("Enter input file name: ");
    scanf("%s", input_file);
    yyin=fopen(input_file,"r");
    yylex();
    fclose(yyin);

    printf("Number of characters: %d\n", charCount);
    printf("Number of words: %d\n", wordCount);
    printf("Number of lines: %d\n", lineCount);
    printf("Number of blanks: %d\n", blankCount);

   
    return 1;
}