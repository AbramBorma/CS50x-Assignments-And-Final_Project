#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

// Global const for the no. of JPEGs.
#define MAX_JPEG_FILES 50

int main(int argc, char *argv[])
{
    // Confirming that the user must write a single command line only.
    if (argc != 2)
    {
        printf("./recover FILE\n");
        return 1;
    }
    // Opening the memory card.
    FILE *card = fopen(argv[1], "r");
    // Reassuring we are not processing through out the code while the card can't be opened.
    if (card == NULL)
    {
        printf("Error Opening the Memory Card\n");
        return 1;
    }

    // Creating a buffer for a block of data.
    uint8_t buffer[512];
    int jpegFileCount = 0;
    FILE *output = NULL;

    // While there's still data left to read from the memory card.
    while (fread(buffer, 1, sizeof(buffer), card) == 512)
    {
        // Condition to start a new JPEG File.
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            char jpegFileName[8];
            // Using sprintf to create a file name using a string.
            sprintf(jpegFileName, "%03i.jpg", jpegFileCount);

            // Close the previous JPEG File if found.
            if (output != NULL)
            {
                fclose(output);
            }
            output = fopen(jpegFileName, "w");

            if (output == NULL)
            {
                printf("Error creating output file");
                return 1;
            }
            // Creating and writing to the first JPEG File.
            fwrite(buffer, 1, sizeof(buffer), output);
            jpegFileCount++;
        }
        // Creating the rest of JPEG Files
        else if (jpegFileCount > 0)
        {
            fwrite(buffer, 1, sizeof(buffer), output);
        }
    }

    if (output != NULL)
    {
        fclose(output);
    }

    // Freeing up memory.
    fclose(card);
    return 0;
}
