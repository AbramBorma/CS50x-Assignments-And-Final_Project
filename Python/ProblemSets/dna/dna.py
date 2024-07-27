import csv
import sys


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


def main():

    # TODO: Check for command-line usage
    if len(sys.argv) != 3:
        print("Invalid Usage. Please enter a Database name and a Sequence")
        sys.exit(1)

    # TODO: Read database file into a variable

    CSV = sys.argv[1]
    rows = []
    with open(CSV, 'r') as db_file:
        reader = csv.DictReader(db_file)
        for row in reader:
            rows.append(row)

    # TODO: Read DNA sequence file into a variable
    seq = sys.argv[2]
    with open(seq, 'r') as seq_file:
        sequence = seq_file.read()

    # TODO: Find longest match of each STR in DNA sequence
    STR = {}
    for key in rows[0].keys():
        if key == "name":
            continue
        STR[key] = longest_match(sequence, key)

    # TODO: Check database for matching profiles
    for row in rows:
        matched = True
        for key in row.keys():
            if key == "name":
                continue
            elif int(row[key]) != STR[key]:
                matched = False
                break
        if matched is True:
            print(row["name"])
            return

    print("No Match")


main()
