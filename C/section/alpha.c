#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main (void)
{
    string name = get_string("What's your name?\n");
    int length = strlen(name);

    for (int i = 0; i < length; i++)
    {
        if (name[i] > name[i-1])
        {
            printf("Yes\n");
        }
        else
        {
            printf("No\n");
        }
    }
}
