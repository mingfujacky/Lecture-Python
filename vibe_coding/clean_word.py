"""
Write a python program to fulfill below requirement
1. word is a string
2. return a version of word in which all letters have been converted to lowercase,
punctuation characters have been stripped from both ends.
3. inner punctuation is left untouched.
4. use doctest to do test cases
"""
def clean_word(word):
    """
    Cleans the input word by converting it to lowercase and stripping punctuation from both ends.

    >>> clean_word("  Hello, World!  ")
    'hello, world'
    >>> clean_word("...Python... ")
    'python'
    >>> clean_word("!!!Test!!!")
    'test'
    >>> clean_word("NoPunctuation")
    'nopunctuation'
    >>> clean_word("  Spaces  ")
    'spaces'
    """
    # Strip leading and trailing whitespace
    word = word.strip()
    
    # Convert to lowercase
    word = word.lower()
    
    # Strip punctuation from both ends
    while len(word) > 0 and not word[0].isalnum():
        word = word[1:]
    while len(word) > 0 and not word[-1].isalnum():
        word = word[:-1]
    
    return word
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)

