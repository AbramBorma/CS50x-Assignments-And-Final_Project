#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main (int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./read infile\n");
        return 1;
    }

    char buffer[7];

    char *plates[8];

    FILE *infile = fopen(argv[1], "r");

    int idx = 0;

    while (fread(buffer, sizeof(char), 7, infile) == 7)
    {
        buffer[6] = '\0';
        plates[idx] = malloc(7 * sizeof(char));
        for (int i = 0; i < 7; i++)
        strcpy(plates[idx], buffer);
        idx++;
    }

    for (int i = 0; i < 8; i++)
    {
        printf("%s\n", plates[i]);
        free(plates[i]);
    }
    fclose(infile);
}
