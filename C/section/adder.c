#include <cs50.h>
#include <stdio.h>

int add_two_ints(int a, int b);

int main (void)
{
    // Prompt user to give the first integer.
    int x = get_int("Give me an Integer: \n");

    // Prompt user to give the second integer.
    int y = get_int("Give me another Integer: \n");

    // Recall the function of adding two integers to use.

    int z = add_two_ints(x, y);

    printf("The sum of %i and %i is %i \n", x, y, z);
}

// Create a Function to add two integers.

int add_two_ints(int a, int b)
{
    int sum;
    sum = a + b;
    return sum;
}
