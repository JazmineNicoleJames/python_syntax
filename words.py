words = ['you','are','amazing','everybody']
must_start_with = ['y','a']

for word in words:
    print(word.upper())

def print_upper_words(words):
    """ Print each word in uppercase and on seperate line. """
    for word in words:
        print(word.upper())

def print_e_upper_words(words):
    """ Print each word that begins with the letter "e", but uppercased. """
    for word in words:
        if word.startswith("e"):
            print(word.upper())

def print_words_with_any_letter(words, must_start_with):
    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())


