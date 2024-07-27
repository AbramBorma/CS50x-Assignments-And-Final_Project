#include <cs50.h>
#include <stdio.h>

int main (void)
{
    int number = 5;
    int guess = get_int("What's your Guess?\n");

    if (number != guess)
    {
        printf("Wrong Guess \n");
    }
    else
    {
        printf("You're Correct \n");
    }
}
