#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

// Points assigned to each letter of the alphabet
int POINTS[] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25};
// int lett[] = {a, b, c, d, e ,f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z};

int compute_score(string word);

int main(void)
{
    // Get input words from both players
    string word1 = get_string("Player 1: ");
    string word2 = get_string("Player 2: ");

    // Score both words
    int score1 = compute_score(word1);
    int score2 = compute_score(word2);

    // TODO: Print the winner
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
}

int compute_score(string word)

{
    char temp;
    int i, h, j, k;
    int score = 0;
    // Function to check if the given word has special characters and remove them.
    for (i = 0; i < strlen(word); i++)
    {
        while (!(word[i] >= 'a' && word[i] <= 'z') && !(word[i] >= 'A' && word[i] <= 'Z'))
        {
            for (h = i; h < strlen(word); h++)
            {
                word[h] = word[h + 1];
            }
        }
        // Function to convert all the capital letters to small letter.
        if (word[i] >= 65 && word[i] <= 90)
        {
            word[i] = word[i] + 32;
        }
    }
    // Function to sort the letter alphabetically inside the string.
    for (k = 0; k < strlen(word); k++)
    {
        for (j = k; j < strlen(word); j++)
        {
            if (word[j] < word[k])
            {
                temp = word[j];
                word[j] = word[k];
                word[k] = temp;
            }
        }
        score += POINTS[word[k] - 97];
    }
    return score;
}
