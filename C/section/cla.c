#include <cs50.h>
#include <stdio.h>

int main (int argc, string argv[])
{
    for (int i = 1; i < argc; i++)
    {
        printf("%c\n", argv [i][0]);
    }

}

    for (int i = 1; i < argc; i++)
    {
        if (argc == 2)
        {
            printf("Usage: %s\n", argv[i]);
        }
        else
        {
            printf("Usage: key\n");
            return false;
        }
    }
}
