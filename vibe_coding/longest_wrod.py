# returns the longest word in a list
def find_longest_word(words):
    """
    Returns the longest word in a list.

    >>> find_longest_word(["apple", "banana", "cherry", "date"])
    'banana'
    >>> find_longest_word(["hi", "hello", "hey"])
    'hello'
    >>> find_longest_word([])
    
    >>> find_longest_word(["a", "bb", "ccc", "dd"])
    'ccc'
    """
    if not words:
        return None
    longest_word = words[0]
    for word in words[1:]:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)