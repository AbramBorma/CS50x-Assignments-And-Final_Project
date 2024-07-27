// Implements a dictionary's functionality

#include <ctype.h>
#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <strings.h>
#include <string.h>

#include "dictionary.h"

unsigned int final_size = 0;

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 17576;

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    int ref = hash(word);
    node *cursor = table[ref];

    while (cursor != NULL)
    {
        if (strcasecmp(word, cursor->word) == 0)
        {
            return true;
        }
        cursor = cursor->next;
    }
    return false;

    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    unsigned int hash = 0;
    int count = 0;

    for (int i = 0; i < LENGTH && word[i] != '\0'; i++)
    {
        if ((isalpha(word[i]) || word[i] == '\'') && count <3)
        {
            hash = (hash * 26) + (toupper(word[i] - 'A'));
            count ++;
        }
    }
    return hash % N;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // TODO
    char copied_word[LENGTH];
    int idx = 0;

    FILE *source = fopen(dictionary, "r");
    if (source == NULL)
    {
        printf("Error opening dictionary\n");
        return false;
    }

    // Read each word in the file
    while(fscanf(source, "%s", copied_word) != EOF)
    {
        for (int i = 0; i < LENGTH; i++)
        {
            if (copied_word[i] == '\n')
            {
                copied_word[i] = '\0';
                idx++;
            }
        }
     // Add each word to the hash table

    node *new_word = malloc(sizeof(node));
    if(new_word == NULL)
    {
        return false;
    }

    strcpy(new_word->word, copied_word);
    int index = hash(copied_word);

    new_word->next = NULL;

    if (table[index] == NULL)
    {
        table[index] = new_word;
    }
    else
    {
        node *current_word = table[index];
        while(current_word != NULL)
        {
            if(strncasecmp(new_word->word, current_word->word, 3) == 0)
            {
                new_word->next = current_word->next;
                current_word->next = new_word;
                break;
            }
            else
            {
                current_word = current_word->next;
            }
            if (current_word == NULL)
            {
                table[index] = new_word;
            }
        }
    }
    final_size++;
}
    // Close the dictionary file
    fclose(source);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    return final_size;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    for (int i = 0; i < N; i++)
    {
        node *cursor = table[i];

        while (cursor != NULL)
        {
            node *tmp = cursor;
            cursor = cursor->next;
            free(tmp);
        }
    }
    for (int i = 0; i < N; i++)
    {
        table[i] = NULL;
    }

    return true;
}
