# Incubyte hiring challenge
# Name - Vedant Kokane 

# Library Management System

## Features
1. **Camel-Casing Convention**: 
   - Camel-Casing has been used for naming all variables.

2. **Constraints Defined**:
   - Proper constraints are defined for each feature to ensure correct functionality:
     - **Adding Books**: Ensures that no book is added with the same ISBN number or the same title as an existing book in the library.
     - **Borrowing Books**: Ensures that the book exists by its title and has not already been borrowed.
     - **Returning Books**: Ensures that the book exists and has already been borrowed before allowing it to be returned.

3. **Classes Defined**:
   - **Book Class**: Manages individual book details such as ISBN, title, author, and publication year.
   - **Library Class**: Handles the collection of books and the operations for adding, borrowing, returning, and displaying books.
   - **Test Class**: Unit tests have been written to validate the functionality of the `Library` class methods.

## Running the Tests
To run the unit tests for this system, use the following command in your terminal:
```bash
python -m unittest Test.py
