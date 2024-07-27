#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

// Points assigned to each letter of the alphabet
int POINTS[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

int compute_score(string word);

int main(void)
{
    // Get input words from both players
    string word1 = get_string("Player 1: ");
    string word2 = get_string("Player 2: ");

    // Score both words
    int score1 = compute_score(word1);
    int score2 = compute_score(word2);

    // Print the winner
    if (score1 > score2)
    {
        printf("Player 1 wins!\n");
    }
    else if (score2 > score1)
    {
        printf("Player 2 wins!\n");
    }
    else
    {
        printf("Tie!\n");
    }

    return 0;
}

int compute_score(string word)
{
    int score = 0;
    int word_length = strlen(word);

    // Function to check if the given word has special characters and remove them
    int i, j;
    for (i = 0, j = 0; i < word_length; i++)
    {
        if ((word[i] >= 'a' && word[i] <= 'z') || (word[i] >= 'A' && word[i] <= 'Z'))
        {
            // Function to convert all the capital letters to small letter
            if (word[i] >= 'A' && word[i] <= 'Z')
            {
                word[j] = word[i] + ('a' - 'A');
            }
            else
            {
                word[j] = word[i];
            }
            j++;
        }
    }
    word[j] = '\0'; // to terminate the modified word

    word_length = strlen(word);

    // Function to sort the letters alphabetically inside the string
    int k;
    for (k = 0; k < word_length; k++)
    {
        int min_index = k;
        for (j = k + 1; j < word_length; j++)
        {
            if (word[j] < word[min_index])
            {
                min_index = j;
            }
        }
        if (min_index != k)
        {
            char temp = word[k];
            word[k] = word[min_index];
            word[min_index] = temp;
        }
        score += POINTS[word[k] - 'a'];
    }
    return score;
}
