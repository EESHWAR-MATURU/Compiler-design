#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_VARIABLES 100
#define MAX_PRODUCTIONS 100
#define MAX_PROD_LENGTH 100

struct CFGParser
{
    int num_variables;
    char variables[MAX_VARIABLES][MAX_PROD_LENGTH];
    char productions[MAX_VARIABLES][MAX_PRODUCTIONS][MAX_PROD_LENGTH];
};

void initialize(struct CFGParser *parser)
{
    printf("Enter the number of non-terminals: ");
    scanf("%d", &parser->num_variables);
    printf("Enter the non-terminals: ");
    for (int i = 0; i < parser->num_variables; i++)
    {
        scanf("%s", parser->variables[i]);
    }

    for (int i = 0; i < parser->num_variables; i++)
    {
        printf("Enter the number of productions for %s: ", parser->variables[i]);
        int num_productions;
        scanf("%d", &num_productions);
        for (int j = 0; j < num_productions; j++)
        {
            printf("Enter the RHS of production: ");
            scanf("%s", parser->productions[i][j]);
        }
    }
}

void to_string(struct CFGParser parser)
{
    printf("%d\n", parser.num_variables);
    for (int i = 0; i < parser.num_variables; i++)
    {
        printf("%s -> ", parser.variables[i]);
        for (int j = 0; j < MAX_PRODUCTIONS; j++)
        {
            if (strlen(parser.productions[i][j]) == 0)
                break;
            printf("%s | ", parser.productions[i][j]);
        }
        printf("\n");
    }
}

void check_left_rec(struct CFGParser parser)
{
    for (int i = 0; i < parser.num_variables; i++)
    {
        for (int j = 0; j < MAX_PRODUCTIONS; j++)
        {
            if (strlen(parser.productions[i][j]) == 0)
                break;
            if (parser.variables[i][0] == parser.productions[i][j][0])
            {
                printf("Left recursion\n");
                printf("%s -> %s\n", parser.variables[i], parser.productions[i][j]);
            }
        }
    }
}

void left_factoring(struct CFGParser *parser)
{
    for (int i = 0; i < parser->num_variables; i++)
    {
        char recursions[MAX_PRODUCTIONS][MAX_PROD_LENGTH];
        char terminals[MAX_PRODUCTIONS][MAX_PROD_LENGTH];
        int recursion_count = 0;
        int terminal_count = 0;
        for (int j = 0; j < MAX_PRODUCTIONS; j++)
        {
            if (strlen(parser->productions[i][j]) == 0)
                break;
            if (islower(parser->productions[i][j][0]))
            {
                strcpy(terminals[terminal_count], parser->productions[i][j]);
                terminal_count++;
            }
            if (parser->variables[i][0] == parser->productions[i][j][0])
            {
                strcpy(recursions[recursion_count], parser->productions[i][j]);
                recursion_count++;
            }
        }
        if (recursion_count == 0)
            continue;
        else
        {
            char arr1[MAX_PRODUCTIONS][MAX_PROD_LENGTH];
            char arr2[MAX_PRODUCTIONS][MAX_PROD_LENGTH];
            int arr1_count = 0;
            int arr2_count = 0;
            if (terminal_count > 0)
            {
                for (int k = 0; k < terminal_count; k++)
                {
                    sprintf(arr1[arr1_count], "%s%s'", terminals[k], parser->variables[i]);
                    arr1_count++;
                }
            }
            else
            {
                sprintf(arr1[arr1_count], "%s'", parser->variables[i]);
                arr1_count++;
            }
            for (int k = 0; k < recursion_count; k++)
            {
                sprintf(arr2[arr2_count], "%s%s'", &parser->productions[i][k][1], parser->variables[i]);
                arr2_count++;
            }
            strcpy(arr2[arr2_count], "E");
            arr2_count++;
            strcpy(parser->productions[i][0], arr1[0]);
            for (int k = 1; k < arr1_count; k++)
            {
                strcpy(parser->productions[i][k], arr1[k]);
            }
            for (int k = 0; k < arr2_count; k++)
            {
                strcpy(parser->productions[parser->num_variables], arr2[k]);
                parser->num_variables++;
            }
        }
    }
}

int main()
{
    struct CFGParser parser;
    initialize(&parser);
    to_string(parser);
    check_left_rec(parser);
    left_factoring(&parser);
    to_string(parser);
    return 0;
}