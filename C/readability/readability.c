#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

// Identification of Global Variables.
string text;
int count_letters(string text1);
int count_words(string text2);
int count_sentences(string text3);

int main(void)
{
    // Getting the text from the user.
    text = get_string("Text: ");

    // Assigning the outputs of the functions to new variables.
    float actLetters = count_letters(text);
    float actWords = count_words(text);
    float actSentences = count_sentences(text);

    // Calculating Coleman-Liau index.
    float(index) = round((0.0588 * (actLetters * 100 / actWords)) - (0.296 * (actSentences * 100 / actWords)) - (15.8));
    int index1 = index / ((float) 1);

    // Printing out the Grade.
    if (index1 >= 16)
    {
        printf("Grade 16+\n");
    }
    else if (index1 < 1)
    {
        printf("Before Grade 1\n");
    }
    else
    {
        printf("Grade %i\n", index1);
    }
}

// Function to Count the no. of letters in the text.
int count_letters(string text1)
{
    int letter = 0;
    int i;
    for (i = 0; i < strlen(text1); i++)
    {
        if ((text1[i] >= 'a' && text1[i] <= 'z') || (text1[i] >= 'A' && text1[i] <= 'Z'))
        {
            letter++;
        }
    }
    return letter;
}

// Function to count the no. of words in the text.
int count_words(string text2)
{
    int word = 1;
    int i;
    for (i = 0; i < strlen(text); i++)
    {
        if (text2[i] == ' ')
        {
            word++;
        }
    }
    return word;
}

// Function to count the no. of sentences in the text.
int count_sentences(string text3)
{
    int sentence = 0;
    int i;
    for (i = 0; i < strlen(text3); i++)
    {
        if ((text3[i] == '.') || (text3[i] == '!') || (text3[i] == '?'))
        {
            sentence++;
        }
    }
    return sentence;
}
