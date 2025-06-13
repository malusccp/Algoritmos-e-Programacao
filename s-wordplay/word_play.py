import utils

def main():
    while True:
        menu_word() 
        choose = int(input('Choose a option: '))
        if choose == no_letter: 
            has_no_letter()
        elif choose == size_of_word:
            size_word()
        elif choose == letter_forbidden:
            forbidden = input('Whats the forbidden letter?:')
            show_word_without_forbbiden_letter(forbidden)
        elif choose == exit: 
            break

def has_no_letter():
    letters = str(input('Choose any letter: '))
    words = open('words.txt')
    all = 0
    find = 0

    for letter in words:
        all += 1
        if not letters in letter:
            word = letter.strip()
            print(word)
            find +=1
    print(f'The percentage of words that has no letter "{letters}" is: {(find/all)*100:.1f}% ')

def size_word():
    size = int(input('What size do you want?: '))
    words = open('words.txt')
    all = 0
    find = 0

    for letter in words:
        all += 1
        if size <= len(letter):
            word = letter.strip()
            print(word)
            find +=1
    print(f'The percentage of words greater than "{size}" is: {(find/all)*100:.1f}% ')

def show_word_without_forbbiden_letter(forbidden):
    file = open('br-sem-acentos.txt')

    for line in file:
        word = line.strip()
        if utils.avoids(word, forbidden):
            print(word)




def menu_word():
    interface = '''
>>> Words Play <<< 
1 - If you want to choose a letter
2 - If you want to choose the size of the word
3 - 


0 - Exit
'''
    print(interface)

# Constantes
no_letter = 1
size_of_word = 2
letter_forbidden = 3
exit = 0

main()