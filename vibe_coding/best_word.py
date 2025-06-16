'''
Return the number of points of a word.
    The points are assigned as follows:
    A, E, I, O, U, L, N, S, T, R = 1 point
    D, G = 2 points
    B, C, M, P = 3 points
    F, H, V, W, Y = 4 points
    K = 5 points
    J, X = 8 points
    Q, Z = 10 points
'''
def get_word_points(word):
    points = 0
    for char in word.upper():
        if char in "AEIOULNSTR":
            points += 1
        elif char in "DG":
            points += 2
        elif char in "BCMP":
            points += 3
        elif char in "FHVWY":
            points += 4
        elif char == "K":
            points += 5
        elif char in "JX":
            points += 8
        elif char in "QZ":
            points += 10
    return points

'''
Return the best word from a list of words based on Scrabble points.
'''
def get_best_word(words):
    best_word = ""
    max_points = 0
    for word in words:
        points = get_word_points(word)
        if points > max_points:
            max_points = points
            best_word = word
    return best_word

print(get_best_word(["hello", "world", "python", "scrabble", "quiz"]))