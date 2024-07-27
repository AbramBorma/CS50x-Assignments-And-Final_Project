#include <cs50.h>
#include <stdio.h>
#include <ctype.h>

float calc_hours(int weeks, int hours[], char required);

int main (void)
{
    // Prompt user to write down the no. of weeks taking the course.
    int weeks;
    do
    {
        weeks = get_int("No. of weeks taking CS50: ");
    }
    while (weeks < 1);

    // identifying the array and storing the no of HW hours in it.
    int hours[weeks];

    for (int i = 0; i < weeks; i++)
    {
        hours[i] = get_int("Week %i HW hours: ", i);
    }

    // Prompt user to select the either the requires is Average or Total
    char required;
    do
    {
        required = toupper(get_char("Enter T for total hours, A for average hours per week: "));
    }
    while (required != 'T' && required != 'A');

    printf("%0.1f hours\n", calc_hours(weeks, hours, required));

}

// Create a function to calculate the total or average no. of HW hours
float calc_hours(int weeks, int hours[], char required)
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
    if (required == 'A')
    {
        average = (sum / (float)weeks);
        return average;
    }
    // Confition to return the total.
    else if (required == 'T')
    {
        return sum;
    }
    else
    {
        return 0;
    }
}
