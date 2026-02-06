import os, random

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
        if 2 < letters <= maxLetters:
            break
        else:
            print(f"Please enter a value between 3 and {maxLetters}.")
    except ValueError:
        print("Please put a number.")

validWords = [x.strip() for x in words if len(x.strip()) == letters]

CORRECT = "\033[42m"       # Green background
WRONG_PLACE = "\033[43m"   # Yello background
WRONG = "\033[40m"         # Black background
RESET = "\033[0m"          # Reset colour

colors = input(CORRECT + "Can you see the background color? (y/n)" + RESET + "\n> ").lower() in ["y", "yes"]
word = random.choice(validWords)

clear()

print("--------- Python Wordle ---------")
print(f"Selected letters: {letters}")
print(word)
print()

while True:
    while True: # Main game loop
        guess = input()
        clearLine()
        truth = ""
        corrects = 0
        for i, x in enumerate(guess):
            if word[i] == x:
                truth += CORRECT + x + RESET
                corrects += 1
            elif x in word:
                truth += WRONG_PLACE + x + RESET
            else:
                truth += WRONG + x + RESET
        print(truth)
        if corrects == letters:
            break
    again = input("Well done!\nAgain? (y/n)\n> ") in ["y", "yes"]
    clear()
    if not again:
        break
