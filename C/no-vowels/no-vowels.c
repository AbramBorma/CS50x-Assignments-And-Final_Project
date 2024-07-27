// Write a function to replace vowels with numbers
// Get practice with strings
// Get practice with command line
// Get practice with switch

#include <cs50.h>
#include <stdio.h>
#include <string.h>

void replace(char argv[]);

int main(int argc, string argv[])
{
    if (argc < 2)
    {
        printf("Error: no command lines are given.\n");
        return 1;
    }
    char *letter = argv[1];
    replace(letter);
    printf("%s\n", letter);
}

void replace(char argv[])
{
    int i;
    for (i = 0; i < strlen(argv); i++)
    {
        switch (argv[i])
        {
            case 'a':
            case 'A':
                argv[i] = '6';
                break;
            case 'e':
            case 'E':
                argv[i] = '3';
                break;
            case 'i':
            case 'I':
                argv[i] = '1';
                break;
            case 'o':
            case 'O':
                argv[i] = '0';
                break;
        }
    }
}
