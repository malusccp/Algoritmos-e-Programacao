def have_char(word, char):
    for char in word:
        if char == word:
            return True
        
    return False
        


def avoids(word, letter_forbidden):
    for char in word:
        if have_char(letter_forbidden, char):
            return False
        
    return True