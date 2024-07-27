#include <cs50.h>
#include <stdio.h>

int main (void)
{
    int n;
    do
    {
        n = get_int("Enter a Number: ");
    }
    while (n < 1);

    int power[n];

    power[0] = 1;

    printf("%i\n", power[0]);

    for (int i = 1; i < n; i++)
    {
        power[i] = 2 * power[i-1];
        printf("%i\n", power[i]);
    }
}
