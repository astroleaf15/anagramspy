import random
import time

# Uword = Unscrambled World
# Sword = Scrambled Word (displayed to the user)
# Tword = Test Word (Used to test if Sword != Uword)
# GuessedWords = Words that have already been guessed (and correct)

class color:
    GREEN = '\033[92m'
    RED = '\033[31m'
    BLUE = '\033[36m'
    END = '\033[0m'

global points
points = 0
GuessedWords = []

def anagram(guess, word):
    guesslist = list(guess)
    wordlist = list(word)
    for i in range(len(guesslist)):
        if guesslist[i] in wordlist:
            wordlist.remove(guesslist[i])
        else:
            print(f"{color.RED}That is not an anagram!{color.END}")
            global Anagram
            Anagram = False
            return

def acceptword(guess):
    aguess = guess + "\n"
    if aguess in GuessedWords:
        print(f"{color.RED}You already guessed that word!{color.END}")
        global Word
        Word = False
        return
    else:
        with open("legalwords.txt") as f:
            lines=f.readlines()
            if aguess in lines:
                GuessedWords.append(aguess)
                if len(guess) == 3:
                    print(f"{color.GREEN}Nice!{color.END}" + f"{color.BLUE} +100 {color.END}")
                elif len(guess) == 4:
                    print(f"{color.GREEN}Good Job!{color.END}" + f"{color.BLUE} +400 {color.END}")
                elif len(guess) == 5:
                    print(f"{color.GREEN}Great Job!{color.END}" + f"{color.BLUE} +1200 {color.END}")
                elif len(guess) == 6:
                    print(f"{color.GREEN}Wow!{color.END}" + f"{color.BLUE} +2000 {color.END}")
                else:
                    print(f"{color.GREEN}You got that WOW factor!{color.END}" + f"{color.BLUE} +5000 {color.END}")
            else:
                print(f"{color.RED}{guess} is not a legal word!{color.END}")
                Word = False
                return

#input a number string; output a list of letters
def numtolet(num):
    n = 2
    if len(num) != 14:
        print(f"{color.RED}That is not a valid number!{color.END} Starting normally...")
        return
    else:
        pass
    global seq
    seq = [(num[i:i+n]) for i in range(0, len(num), n)]
    seq = list(map(int, seq))
    for i in range(len(seq)):
        if seq[i] > 26:
            print(f"{color.RED}That is not a valid number!{color.END} Starting normally...")
            return
        else:
            pass
    else:
        pass
    for i in range(len(seq)):
        if seq[i] == 1:
            seq[i] = "a"
        elif seq[i] == 2:
            seq[i] = "b"
        elif seq[i] == 3:
            seq[i] = "c"
        elif seq[i] == 4:
            seq[i] = "d"
        elif seq[i] == 5:
            seq[i] = "e"
        elif seq[i] == 6:
            seq[i] = "f"
        elif seq[i] == 7:
            seq[i] = "g"
        elif seq[i] == 8:
            seq[i] = "h"
        elif seq[i] == 9:
            seq[i] = "i"
        elif seq[i] == 10:
            seq[i] = "j"
        elif seq[i] == 11:
            seq[i] = "k"
        elif seq[i] == 12:
            seq[i] = "l"
        elif seq[i] == 13:
            seq[i] = "m"
        elif seq[i] == 14:
            seq[i] = "n"
        elif seq[i] == 15:
            seq[i] = "o"
        elif seq[i] == 16:
            seq[i] = "p"
        elif seq[i] == 17:
            seq[i] = "q"
        elif seq[i] == 18:
            seq[i] = "r"
        elif seq[i] == 19:
            seq[i] = "s"
        elif seq[i] == 20:
            seq[i] = "t"
        elif seq[i] == 21:
            seq[i] = "u"
        elif seq[i] == 22:
            seq[i] = "v"
        elif seq[i] == 23:
            seq[i] = "w"
        elif seq[i] == 24:
            seq[i] = "x"
        elif seq[i] == 25:
            seq[i] = "y"
        else:
            seq[i] = "z"

#input a letter string; output a list of numbers
def lettonum(let):
    for i in range(len(let)):
        if let[i] == "a":
            let[i] = "01"
        elif let[i] == "b":
            let[i] = "02"
        elif let[i] == "c":
            let[i] = "03"
        elif let[i] == "d":
            let[i] = "04"
        elif let[i] == "e":
            let[i] = "05"
        elif let[i] == "f":
            let[i] = "06"
        elif let[i] == "g":
            let[i] = "07"
        elif let[i] == "h":
            let[i] = "08"
        elif let[i] == "i":
            let[i] = "09"
        elif let[i] == "j":
            let[i] = "10"
        elif let[i] == "k":
            let[i] = "11"
        elif let[i] == "l":
            let[i] = "12"
        elif let[i] == "m":
            let[i] = "13"
        elif let[i] == "n":
            let[i] = "14"
        elif let[i] == "o":
            let[i] = "15"
        elif let[i] == "p":
            let[i] = "16"
        elif let[i] == "q":
            let[i] = "17"
        elif let[i] == "r":
            let[i] = "18"
        elif let[i] == "s":
            let[i] = "19"
        elif let[i] == "t":
            let[i] = "20"
        elif let[i] == "u":
            let[i] = "21"
        elif let[i] == "v":
            let[i] = "22"
        elif let[i] == "w":
            let[i] = "23"
        elif let[i] == "x":
            let[i] = "24"
        elif let[i] == "y":
            let[i] = "25"
        else:
            let[i] = "26"
    global out
    out = ""
    for x in let:
        out += x

with open("sevenletterwords.txt") as f:
    lines = f.readlines()
    Uword = random.choice(lines)

Sword = list(Uword)
Tword = list(Uword)
Sword.remove("\n")
Tword.remove("\n")
while Sword == Tword:
    random.shuffle(Sword)

code = input("Do you have a code? (Y/N): ")
if code == "Y" or code == "y":
    number = input("Enter the 14 digit code: ")
    numtolet(number)
    Sword = seq
    Uword = ""
    for x in Sword:
        Uword += x
elif code == "N" or code == "n":
    pass
else:
    print(f"{color.RED}That is not a valid answer!{color.END} Starting normally...")

p = time.time() + 30

on = 1
while on == 1:
    out_str = " "
    print(out_str.join(Sword).upper())
    Anagram = True
    Word = True

    guess = input("Enter your word: ")
    guess = guess.lower()


    if p >= time.time():
        anagram(guess, Uword)

        if Anagram == False:
            Word = False
            pass
        else:
            acceptword(guess)

        if Word == True:
            if len(guess) == 3:
                points += 100
            elif len(guess) == 4:
                points += 400
            elif len(guess) == 5:
                points += 1200
            elif len(guess) == 6:
                points += 2000
            else:
                points += 5000
        print("Points: " + f"{color.BLUE}{points}{color.END}" + "\n")
    else:
        break

lettonum(Sword)
print("\n" + "Time's up!")
print("Final Score: " + f"{color.BLUE}{points} Points{color.END}")
print("Share this code to challenge your friends: " + f"{color.BLUE}{out}{color.END}")