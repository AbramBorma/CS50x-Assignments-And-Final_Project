#include <cs50.h>
#include <stdio.h>

int factorial(int number);

int main (void)
{
    int n = get_int("Enter a Number: ");
    printf("Factorial is: %i\n", factorial(n));
}

int factorial(int number)
{
    if (number == 1)
    {
        return 1;
    }
    return number * factorial(number - 1);
    //int solution = number;
    //for(int i = number - 1; i > 0; i--)
    //{
        //solution = solution * i;
    //}
    //return solution;
}
