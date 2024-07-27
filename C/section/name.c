#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main (void)
{
    string name = get_string ("What's your name?\n");
    int length = strlen(name);

    printf("Welcome ");

    for (int i = 0; i < length; i++)
    {
        printf("%i ", name[i]);
    }
    printf("\n");
}
