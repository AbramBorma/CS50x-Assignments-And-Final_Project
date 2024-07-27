// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>

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

    // Traverse the linked list.
    while (cursor != NULL)
    {
        // Compare the word with the word in the current node.
        if (strcasecmp(word, cursor->word) == 0)
        {
            return true;
        }
        cursor = cursor->next;
    }
    free(cursor);
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
        // Checking if the letters are Alphabetic or Apostrophe.
        if ((isalpha(word[i]) || word[i] == '\'') && count < 3)
        {
            hash = (hash * 26) + (toupper(word[i]) - 'A');
            count++;
        }
    }
    // Returning the hash value with consideration to the N.
    return hash % N;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // TODO
    char copied_word[LENGTH + 1];
    int idx = 0;
    int index;

    FILE *source = fopen(dictionary, "r");
    if (source == NULL)
    {
        printf("Error opening dictionary\n");
        return false;
    }

    // Read each word in the file
    while (fscanf(source, "%s", copied_word) != EOF)
    {

        // Creating a node for each word

        node *new_word = malloc(sizeof(node));
        if (new_word == NULL)
        {
            fclose(source);
            return false;
        }

        new_word->next = NULL;

        // Copying the words into the nodes.
        strcpy(new_word->word, copied_word);

        // Computing the hash value for the nodes.
        index = hash(copied_word);

        new_word->next = table[index];
        table[index] = new_word;

        // Updating the size of counted words.
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

        // Traversing the linked lists and freeing all the nodes.
        while (cursor != NULL)
        {
            node *tmp = cursor;
            cursor = cursor->next;
            free(tmp);
        }
        // Freeing the table.
        table[i] = NULL;
    }
    return true;
}
