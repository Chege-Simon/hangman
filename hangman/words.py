#open file and fetch word randomly
import random

def random_word():
    wordFile = "wordlist.txt"

    words = open(wordFile, 'r')

    random_num = random.randrange(0,999)

    wordlist = []
    for word in words:
        wordlist.append(word.strip().lower())

    current_word = wordlist[random_num]
    return current_word
