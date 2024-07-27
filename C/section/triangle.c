#include <cs50.h>
#include <stdio.h>

int valid_triangle(int x, int y, int z);
int main (void)
{
    // Prompt user to get the length of the first side.
    int a, b, c;
    do
    {
        a = get_int("First Side Length: \n");
        b = get_int("Second Side Length: \n");
        c = get_int("Third Side Length: \n");
    }
    while (a < 1 || b < 1 || c < 1);

    string s = int valid_triangle(a, b, c);

    printf("%s \n", s);

}

int valid_triangle(int x, int y, int z)
{
    int sum = x + y + z;
    if (sum < 0 || ((x + y) <= z) || ((x + z) <= y) || ((y + z) <= x))
    {
        printf("The triangle is Invalid\n");
    }
    else
    {
        printf("The Triangle is Valid\n");
    }
}
