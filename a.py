"""The comments writtern after functions and in the first line will be shown as help
to check this type python then press RETURN and then import filename for example for this file 
enter import a then type help(a) or help(a.broken_words) and see magic"""
def broken_words(sentence):
    """This method will take a string sentence as input and
return a list conatining the words in sentence"""
    words = sentence.split(' ')
    return words




def sort_words(words):
    """This method will take a list as input and return the 
list after sorting it"""
    words = sorted(words)
    return words



def print_first_word(words):
    """This method will take a list as input and it will POP
the first word form the list and print that word"""
    word = words.pop(0)
    print word



def print_last_word(words):
    """This method will take a list as input and it will POP
the last word from the list and print that word"""
    word = words.pop(-1)
    print word



def print_first_sorted_word(sentence):
    """This method will take a input string and it will break
the sentence into list and will sort the list and then POP the
first word from the sorted list and then print that word"""
    words = broken_words(sentence)
    words = sort_words(words)
    word = words.pop(0)
    print word



def print_last_sorted_word(sentence):
    """This method will take a input string and it will break
the sentence into list and will sort the list and then POP the
last word from the sorted list and then print the word"""
    words = broken_words(sentence)
    words = sort_words(words)
    word = words.pop(-1)
    print word
