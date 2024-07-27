#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

string text;


int count_words(string text2);

int main(void)
{
    text = get_string("Text: ");
    printf("%i words\n", count_words(text));
}

int count_words(string text2)
{
    int length1 = 0;
    string words = strtok(text2, " ");
    while (words != NULL)
    {
        length1++;
        words = strtok(NULL, " ");
    }
    return length1;
}
