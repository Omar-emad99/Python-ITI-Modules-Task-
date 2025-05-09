Python Utility Scripts
This repository contains a collection of Python scripts that perform various utility functions, including email validation, vowel counting, login authentication, pyramid generation, multiplication tables, and number sorting.

Scripts Overview
emails.py

Validates email addresses with a user-friendly retry mechanism (max attempts configurable).

Checks for basic email format requirements (user@domain.tld).

Letters.py

VowelsCount(): Counts and displays the occurrences of each vowel in a given string.

iCount(): Finds and returns the positions of the letter 'i' in a string (case-insensitive).

login.py

Authenticates users against a mock database (list of dictionaries).

Checks username and password matches.

MarioPyramid.py

strin(): Prints a right-aligned pyramid of asterisks using string manipulation.

listed(): Generates the same pyramid using list operations.

MultiplicationTable.py

Triangle(): Prints a triangular multiplication table up to a given number.

listed(): Generates the same table as a nested list.

Sorting.py

numbers5(): Prompts the user to input 5 numbers, validates them, and returns sorted lists in ascending and descending order.

main.py

Demonstrates usage of the other scripts (commented out by default). Uncomment sections to test specific functionalities.

How to Use
Clone the repository.

Run main.py and uncomment the relevant sections to test specific scripts.

Alternatively, import individual modules into your own projects as needed.

Notes
Error handling is included in most functions (e.g., invalid input checks).

Some scripts include interactive prompts for user input.
