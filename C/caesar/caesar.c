#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

bool only_digit(string s);

string rotate(string p, int n);

int main(int argc, string argv[])
{
    // Checking if the user use one command line argument or more.
    int k;
    if (argc != 2)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
    else
    {
        if (only_digit(argv[1]) == 1)
        {
            return 1;
        }
    }

    // Function to convert the string number to integer number.
    k = atoi(argv[1]);

    string plaintext = get_string("Plaintext: ");

    printf("Ciphertext: %s\n", rotate(plaintext, k));
}

// Function to check if the command line argument is all digits or not.
bool only_digit(string s)
{
    bool allDigits = true;
    for (int j = 0; j < strlen(s); j++)
    {
        if (!isdigit(s[j]))
        {
            allDigits = false;
            break;
        }
    }

    if (!allDigits)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
    else
    {
        printf("Usage: %s\n", s);
        return 0;
    }
}

// Function to rotate the plain text with the code.
string rotate(string p, int n)
{
    int i;
    // First time to use malloc function ans I used it to allocate a space in memory for the string.
    string c = malloc(strlen(p) + 1);

    for (i = 0; i < strlen(p); i++)
    {
        if (isalpha(p[i])) // Check if the character is alphabetic
        {
            char base;
            if (islower(p[i])) // Check which base to follow; a-z or A-Z?
            {
                base = 'a';
            }
            else
            {
                base = 'A';
            }
            c[i] = (p[i] - base + n) % 26 + base; // Rotate the character based on the determined base.
        }
        else
        {
            c[i] = p[i];
        }
    }
    c[i] = '\0';
    return c;
}
