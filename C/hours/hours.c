#include <cs50.h>
#include <ctype.h>
#include <stdio.h>

float calc_hours(int hours[], int weeks, char output);

int main(void)
{
    int weeks = get_int("Number of weeks taking CS50: ");
    int hours[weeks];

    for (int i = 0; i < weeks; i++)
    {
        hours[i] = get_int("Week %i HW Hours: ", i);
    }

    char output;
    do
    {
        output = toupper(get_char("Enter T for total hours, A for average hours per week: "));
    }
    while (output != 'T' && output != 'A');

    printf("%.1f hours\n", calc_hours(hours, weeks, output));
}

// TODO: complete the calc_hours function
float calc_hours(int hours[], int weeks, char output)
{
    int j;
    int sum = 0;
    float average;

    // Calculation of the sum.
    for (j = 0; j < weeks; j++)
    {
        sum = sum + hours[j];
    }
    // Confition to return the Average.
    if (output == 'A')
    {
        average = (sum / (float) weeks);
        return average;
    }
    // Confition to return the total.
    else if (output == 'T')
    {
        return sum;
    }
    else
    {
        return 0;
    }
}
