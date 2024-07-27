#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

int main(int argc, string argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }

    for (int j = 0; j < strlen(argv[1]); j++)
    {
        if (!isdigit(argv[1][j]))
        {
            printf("Usage: ./caesar key\n");
            return 1;
        }
    }

    printf("Usage: %s\n", argv[1]);
    return 0;
}



#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

bool only_digit(string s)

int main(int argc, string argv[])
{
    int k;
    if (argc != 2)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }

}

bool only_digit(string s)
{
    for (int j = 0; j < strlen(argv[1]); j++)
    {
        if (!isdigit(argv[1][j]))
        {
            printf("Usage: ./caesar key\n");
            return 1;
        }
        else
        {
            //printf("Usage: %s\n", argv[1]);
            k = atoi(argv[1]);
            printf("%i\n", k);
            return 0;
        }
    }
}





bool only_digit(string s)
{
    for (int j = 0; j < strlen(s); j++)
    {
        if (!isdigit(s[j]))
        {
            printf("Usage: ./caesar key\n");
            return 1;
        }
        else
        {
            printf("Usage: %s\n", s);
        }
    }
    return 1;
}





#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

bool only_digit(string s);

int main(int argc, string argv[])
{
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

    k = atoi(argv[1]);

    string plaintext = get_string("Plaintext: ");

    // Additional code for processing plaintext

    return 0;

}

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
