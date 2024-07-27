from cs50 import get_string


def main():
    # Getting the text from the user.
    text = get_string("Text: ")

    # Assigning the outputs of the functions to new variables.
    act_letters = count_letters(text)
    act_words = count_words(text)
    act_sentences = count_sentences(text)

    # Calculating Coleman-Liau index.
    index = round((0.0588 * (act_letters * 100 / act_words)) - (0.296 * (act_sentences * 100 / act_words)) - (15.8))

    index1 = index / float(1)

    # Printing out the Grade.
    if index1 >= 16:
        print("Grade 16+")
    elif index1 < 1:
        print("Before Grade 1")
    else:
        print(f"Grade {index1}")

# Function to Count the no. of letters in the text.


def count_letters(text):
    letters = 0

    for i in text:
        if i.isalpha():
            letters += 1

    return letters

# Function to count the no. of words in the text.


def count_words(text):
    words = 0

    for i in text:
        if i.isspace():
            words += 1

    return words + 1

# Function to count the no. of sentences in the text.


def count_sentences(text):
    sentences = 0

    for i in text:
        if i in ['.', '!', '?']:
            sentences += 1

    return sentences


main()
