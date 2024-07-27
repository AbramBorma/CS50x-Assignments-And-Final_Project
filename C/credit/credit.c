#include <stdio.h>
#include <cs50.h>


int main (void)
{
    // Identifying the variables.
    long number;

    // Prompt User to ge the credit card number.
    do
    {
        number = get_long("Number: ");
    }
    while (number < 1000000000000 || number > 9999999999999999);






}




