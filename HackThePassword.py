import random

print('''Welcome to Hacking!
Try to fiqure out what the password is
by guessing a word from the following list. 
You have three tries to hack the password. Good luck!\n''')

index = random.randint(0,4)
tries = 3
passwords = ["pineapple", "tree", "monkey", "secret", "password"]

for word in passwords:
    print(word)
    
print("\n")

while tries > 0:
    print("You have " + str(tries) + " tries left\n")
    guess = input("Enter your guess: ")
    if passwords[index] == guess:
        print("Congrats! You hacked the password")
        break
    else:
        tries = tries -1
        print("Not quite right")
        if tries > 0:
            print("Guess again!\n")
        else:
            print("Game over!")
        

