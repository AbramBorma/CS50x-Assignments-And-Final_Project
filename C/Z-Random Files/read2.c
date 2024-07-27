#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

string text;

int count_letters(string text1);
int count_words(string text2);
int count_sentences(string text3);

int main(void)
{
    text = get_string("Text: ");

    int actLetters = count_letters(text);
    int actWords = count_words(text);
    int actSentences = count_sentences(text);

    float (index) = round((0.0588 * (actLetters*100/actWords)) - (0.296 * (actSentences*100/actWords)) - (15.8));
    int index1 = index / ((float)1);

    //printf("%i Letters\n", count_letters(text));
    //printf("%i words\n", count_words(text));
    //printf("%i sentences\n", count_sentences(text));

    if (index1 >= 16)
    {
        printf("Grade %i\n", index1);
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

int count_words(string text2)
{
int word = 1;
int i;
for (i = 0; i < strlen(text); i++ )
if (text2[i] == ' ')
{
    word++;
}
return word;
}
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
