"""This function will break the senetence into a list (array in C) named as words"""
def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words




""" sort_words will sort the words list"""
def sort_words(words):
    """Sorts the words."""
    return sorted(words)




""" This function will pop the first word from the list words"""
def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print word




""" This function will pop the last word from the list words"""
def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print word




""" This function will sort the sententce by first braking into list then sorting it"""
def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)




""" This function will pop and print the first and last word by braking sentence into
words list"""
def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)




"""This function will pop and print the first and last word by braking sentence into
words list and then sorting it"""
def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
