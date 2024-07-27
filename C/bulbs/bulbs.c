#include <cs50.h>
#include <stdio.h>
#include <string.h>

const int BITS_IN_BYTE = 8;

void print_bulb(int bit);

int main(void)
{
    // Prompt the user to write a message.
    string message = get_string("Message: ");
    int length = strlen(message);
    // Declaration of an int array to store the ascii decimal values of the message letters in it.
    int ascii[length];

    int i, j, k, decimal, remainder;
    // Declaration of an int array to store the binary value after conversion in it.
    int bin[BITS_IN_BYTE];

    // A For Loop to obtain the ascii value from the message, store it in the int array and assign it to int decimal used for
    // division later.
    for (i = 0; i < length; i++)
    {
        ascii[i] = (int) message[i];
        decimal = ascii[i];

        // Division operation using the modulo% and storing the binary values in the binary array.
        for (j = 0; j < BITS_IN_BYTE; j++)
        {

            remainder = (decimal % 2);
            bin[j] = remainder;
            decimal /= 2;
        }
        // Reversing the resulted binary no. as it's in the opposite direction and calling the print_bulb function.
        for (k = BITS_IN_BYTE - 1; k >= 0; k--)
        {
            print_bulb(bin[k]);
        }

        printf("\n");
    }
}

void print_bulb(int bit)
{
    if (bit == 0)
    {
        // Dark emoji
        printf("\U000026AB");
    }
    else if (bit == 1)
    {
        // Light emoji
        printf("\U0001F7E1");
    }
}
