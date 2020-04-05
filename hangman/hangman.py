from words import random_word
import sys
word = random_word()
tries = 0

def check_attempts(tries):
    #here the number of attempts remaining are tracked 
    previous_guess = []
    phrase = ""
    while tries > 0:
        tries = tries - 1
        phrase1 = ""
        print("Previous guess were: {0}\n".format(previous_guess))
        print("Number of tries remaining: {}\n\n".format(tries))
        print("Your word is: {0}".format(phrase))
        attempt = input("Enter your guess: ")
         # here the users guesses the letters and they are checked if they are in the word
        previous_guess.append(attempt)
        present = attempt in word
        if present:
            for letter in word:
                if letter != attempt:
                    if letter not in phrase:
                        letter = "*"
                    phrase1 = phrase1 + letter
                elif letter == attempt or letter in phrase:
                    phrase1 = phrase1 + letter
            phrase = phrase1
            print("The word is now: {0}".format(phrase))
            print("***************************************")
            if str(phrase) == str(word):
                print("Congratulations, you have solved the word puzzle!")
                print("The word is {0}".format(word))
                sys.exit()

        elif not present:
            print("\nOops, the letter is not in the word")
            print("The word is now: {0}\n".format(phrase))
            continue
    else:
        print("\n\nYou have run out of tries!")
        print("Do you wish to start again")
        restart = input("Yes or No >>>")
        if "y" in restart:
            main()
        else:
            sys.exit()



def gamePlay(word,tries):
    print("Selecting word.......\n\n\n")
    print("The random word has {0} letters".format(len(word)))
    print("The word is: " + "*"*(len(word)))
    check_attempts(tries)

def intro():
    print("""
    Welcome to hangman,
    In this game a random word is generated
    You guess letter by letter what the word could be.
    """)
    while True:
        num_attempts = input("How many attemts bewtween 1 and 25 would you wish to have?")
        try:
            num_attempts = int(num_attempts)
            if 1 <= num_attempts <= 25:
                global tries
                tries = num_attempts
                print("Your attempts are: {0}".format(tries))
                return tries
            else:
                print("{0} is not between 1 and 25".format(num_attempts))
        except ValueError:
            print("{0} is not an integer between 1 and 25".format(num_attempts))

def main():
    intro()
    gamePlay(word,tries)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n\nCtrl + C was pressed, Exiting program!")


