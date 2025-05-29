def words_count(text):
    """
    Counts the number of words in a given text.
    
    Args:
        text (str): The text to count words in.
        
    Returns:
        int: The number of words in the text.
    """
    return len(text.split())    

def characters_count(text):
    """
    Counts the number of characters in a given text.
    
    Args:
        text (str): The text to count characters in.
        
    Returns:
        int: The number of characters in the text.
    """
    lower_text = text.lower()
    char_list = list(lower_text)
    char_count = {char: char_list.count(char) for char in set(char_list)}
    return char_count

def create_report(text):
    """
    Creates a report of the text statistics.
    
    Args:
        text (str): The text to analyze.
        
    Returns:
        dict: A dictionary containing the word count and character count.
    """
    print("=================BOOKBOT===================")
    print("Analyzing book found at 'books/frankenstein.txt'")
    print("------------------Word Count----------------")
    print(f"Found {words_count(text)} total words.")
    print("----------------Character Count---------------")
    char_count = characters_count(text)
    for char, count in sorted(char_count.items()):
        print(f"{char}: {count}")