#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int convert(string input);

int main(void)
{
    string input = get_string("Enter a positive integer: ");

    for (int i = 0, n = strlen(input); i < n; i++)
    {
        if (!isdigit(input[i]))
        {
            printf("Invalid Input!\n");
            return 1;
        }
    }

    // Convert string to int
    printf("%i\n", convert(input));
}

int convert(string input)
{
    // TODO
    int length = strlen(input);

    // Setting the base for the recursive function

    if (length == 1)
    {
        return input[0] - '0';
    }

    // Creating a variable of type char for the last digit in the string.
    char last_num = input[length - 1];

    // Converting the char into int by subtracting - the corresponding value from ASCII table.
    int converted_last_num = last_num - '0';

    // Moving the null terminator one position to the left.
    input[length - 1] = '\0';

    // The recursive function.
    return converted_last_num + 10 * convert(input);
}
