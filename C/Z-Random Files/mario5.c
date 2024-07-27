#include <cs50.h>
#include <stdio.h>

int get_size (void);
void print_grid (int n);

int main(void)
{
    int n = get_size();
    print_grid (n);
}
    int get_size (void)
    {
            int n;
            do
            {
                n = get_int("Size: ");
            }
            while (n < 1 || n > 8);
            return n;
    }

    void print_grid (int n)
    {
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





#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // TODO: Prompt for start size
    int start;
    do
    {
        start = get_int("Start Size: ");
    }
    while (start < 9);
    // TODO: Prompt for end size
    int end;
    do
    {
        end = get_int("End Size: ");
    }
    while (end < start);
    // TODO: Calculate number of years until we reach threshold
    int years = 0;
    do
    {
        start = start + (start/3) - (start/4);
        years++;
    }

        while (start < end);
    // TODO: Print number of years
            printf("%i\n", years);
}























    long number;
    do
    {
        number = get_long("Number: ");
    }
    while (number < 1000000000000 || number > 9999999999999999);










     temp = credit[0];
           for (i = 0; i < 16; i++)
            {
                credit[i-1] = credit[i];
            }
               credit[15] = temp;



    for (j = 0; j < 16; j++)
    {
        temp = credit[0];
        credit[i-1] = credit[i];
        credit[15] = temp;
    }


        printf("The modified array is: \n");
        for (i = 0; i < 16; i++)
        printf("%d ", credit[i]);


    for (i = 0; i < 16; i++)
    {
        credit[i] = number % 10;
        number = number / 10;
        printf("%d ", credit[i]);


            int n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11, n12, n13, n14, n15, n16;

    n1 = ((number % 10)/1)*2;
    n2 = ((number % 100)/10)*2;
    n3 = ((number % 1000)/100)*2;
    n4 = ((number % 10000)/1000)*2;
    n5 = ((number % 100000)/10000)*2;
    n6 = ((number % 1000000)/100000)*2;
    n7 = ((number % 10000000)/1000000)*2;
    n8 = ((number % 100000000)/10000000)*2;
    n9 = ((number % 1000000000)/100000000)*2;
    n10 = ((number % 1000000000)/1000000000)*2;
    n11 = ((number % 10000000000)/10000000000)*2;
    n12 = ((number % 100000000000)/100000000000)*2;
    n13 = ((number % 1000000000000)/1000000000000)*2;
    n14 = ((number % 10000000000000)/10000000000000)*2;
    n15 = ((number % 100000000000000)/100000000000000)*2;
    n16 = ((number % 1000000000000000)/1000000000000000)*2;
    int sum1 = n1 + n3 + n5 + n7 + n9 + n11 + n13 + n15;
    int sum2
