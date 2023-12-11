import random


def number_guesser():
    number = random.randint(1, 10)
    guess = ""
    correctGuess = False
    while correctGuess == False:
        print("Please enter a number 1-10")
        guess = int(input())

        if guess == number:
            correctGuess = True
        else:
            print("That is Incorrect")
    
    print("That is correct!")


number_guesser()



def number_guesser_with_lives():
    lives = 3
    dead = False
    number = random.randint(1, 10)
    guess = ""
    correctGuess = False
    while correctGuess == False and dead == False:
        print("Please enter a number 1-10")
        guess = int(input())

        if guess == number:
            correctGuess = True
        else:
            lives = lives - 1
            print("That is Incorrect, You have", lives, "Lives Left")
            if lives == 0:
                dead = True
    
    if lives > 0 and dead == False:
        print("Good job!")
    else:
        print("Better Luck Next Time")

number_guesser_with_lives()



def is_coin(coin):
    if coin in [1, 5, 10, 15, 25, 50, 100]:
        return True
    else:
        return False



def vending_machine():
    AmountDue = 50
    Balance = 0
    Paid = False
    currentCoin = 0
    if Balance >= AmountDue:
        Paid = True
    while Paid == False:
        print("Amount Due", AmountDue)
        print("Balance", Balance)
        print("Please enter a coin")
        currentCoin = int(input())
        if is_coin(currentCoin) == True:
            Balance = Balance + currentCoin
        else:
            print("---->Not a coin<----")
        if Balance >= AmountDue:
            Paid = True

    print("Thank you for your Purchase")


vending_machine()

