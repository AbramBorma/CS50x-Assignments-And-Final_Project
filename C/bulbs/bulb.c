#include <cs50.h>
#include <stdio.h>
#include <string.h>

const int BITS_IN_BYTE = 8;

int main(void)
{
    // TODO
    string message = get_string ("Message: ");
    int length = strlen(message);
    int ascii[length];

    int i, j, k, decimal, remainder;

    for (i = 0; i < length; i++)
    {
        ascii[i] = (int)message[i];

        int binary[BITS_IN_BYTE];

        for (j = 0; j < BITS_IN_BYTE; j++)
        {
            decimal = ascii[i];
            remainder = (decimal % 2);
            binary[j] = remainder
            decimal /= 2;
            binary[8] = '\0'; // Null-terminate the binary string

            for (k = 7; k >= 0; k--)
            {
                printf_bulb(binary[k]);
            }

        }
    }

}
