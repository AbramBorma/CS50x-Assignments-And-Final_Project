#include <cs50.h>
#include <stdio.h>

// Declaration of the used Functions.
int get_size (void);
void print_grid (int n);

// Abstraction of the functions.
int main(void)
{
    int n = get_size();
    print_grid (n);
}
// Definition of the "get_size" function to determine the required size of the grid.
int get_size(void)
{
    int n;
    do
    {
        n = get_int("Size: ");
    }
    while (n < 1 || n > 8);
    return n;
}
// Definition of the "print_grid" function to print the grip.
void print_grid (int n)
{
    // The first nested loop to print "mario-less".
    for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
                if (i + j < n - 1)
                {
                    printf(" ");
                }
                else
                {
                    printf("#");
                }
            }
            // The other loops to print the rest of "mario-more"
            for (int m = 0; m < 2 ; m++)
                {
                    printf(" ");
                }

            for (int b = 0; b <=i; b++)
                {
                    printf("#");
                }
            printf("\n");
        }
}



