#include <cs50.h>
#include <stdio.h>

typedef struct
{
    string name;
    int votes;
}
candidate;

candidate get_candidate(string prompt);

int main (void)
{
    candidate array_candidates[3];

    for (int i = 0; i < 3; i++)
    {
        array_candidates[i] = get_candidate("Enter a Candidate: ");
    }
    printf("%s\n", array_candidates[1].name);
    printf("%i\n", array_candidates[1].votes);
}

candidate get_candidate(string prompt)
{
    printf("%s\n", prompt);

    candidate c;

    c.name = get_string ("Enter a Name: ");
    c.votes = get_int ("Enter no. of Votes: ");

    return c;
}
