import os, random, time

clear = lambda: os.system('cls' if os.name=='nt' else 'clear')
clearLine = lambda: print("\033[1A\033[2K\r", end="")

try:
    with open("allWords.txt", "r") as f:
        words = f.readlines()
except FileNotFoundError:
    exit("No word file found, please ensure you have downloaded the whole project.")

maxLetters = max(map(len, words))

while True:
    try:
        letters = int(input("Please enter the amount of letters in the word you would like to guess:\n> "))
        if not 2 < letters <= maxLetters:
            print(f"Please enter a value between 3 and {maxLetters}.")
            continue
        break
    except ValueError:
        print("Please put a number.")

validWords = [x.strip() for x in words if len(x.strip()) == letters]

CORRECT = "\033[42m"       # Green background
WRONG_PLACE = "\033[43m"   # Yellow background
WRONG = "\033[40m"         # Black background
RESET = "\033[0m"          # Reset colour

colors = input(CORRECT + "Can you see the background color? (y/n)" + RESET + "\n> ").lower() in ["y", "yes"]

if not colors:
    print("Havent added functionality for this yet lmao. Skill issue")
    exit("Skill issue")

word = random.choice(validWords)

clear()

print("--------- Python Wordle ---------")
print(f"Selected letters: {letters}")
print()

while True:
    while True: # Main game loop
        while True:
            guess = input().strip()
            if len(guess) != letters:
                print("Please guess the correct amount of letters!")
                time.sleep(2)
                clearLine()
                continue
            break
        clearLine()
        truth = ""
        corrects = 0
        lets = {w: a for w, a in zip(word, [word.count(x) for x in word])} # word: appearences // useful for yellow marking (if word has only 1 of a letter only
        for i, x in enumerate(guess):                                                                                         # mark it once, etc.)
            if word[i] == x:
                truth += CORRECT + x + RESET
                corrects += 1
                lets[x] -= 1
            elif x in word and lets[x] > 0:
                truth += WRONG_PLACE + x + RESET
                lets[x] -= 1
            else:
                truth += WRONG + x + RESET
        print(truth)
        if corrects == letters:
            break
    again = input("Well done!\nAgain? (y/n)\n> ") in ["y", "yes"]
    clear()
    if not again:
        break
