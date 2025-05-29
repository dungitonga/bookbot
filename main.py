import os,sys
# main.py
"""
Main module to read a book file and generate a report on its content.
It counts the number of words and characters in the book text.
"""
from stats import words_count, characters_count, create_report

def get_book_text(book_path):
    """
    Reads the content of a book file and returns it as a string.
    
    Args:
        book_path (str): The path to the book file.
        
    Returns:
        str: The content of the book file.
    """                    
    with open(book_path, 'r', encoding='utf-8') as file:
        book_text = file.read()
    return book_text   


def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <path_to_book_file>")
        sys.exit(1)      
    else:
        book_path = sys.argv[1]  # Get the book path from command line arguments
    if not os.path.exists(book_path):
        print(f"Error: The file '{book_path}' does not exist.")
        book_path = 'books/frankenstein.txt'  # Default book path if not provided or invalid

    # Read the book text and create a report
    book_text = get_book_text(book_path)
    create_report(book_text)

if __name__ == "__main__":
    main()