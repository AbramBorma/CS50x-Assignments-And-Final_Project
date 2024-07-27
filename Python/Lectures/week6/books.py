books = []

for i in range(3):
    book = dict()
    book["Author"] = input("Enter an Author: ")
    book["Title"] = input("Enter a Title: ")
    books.append(book)

for book in books:
    print(f"{book['Author']} wrote {book['Title']}.")
