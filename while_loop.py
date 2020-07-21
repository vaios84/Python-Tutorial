secretNumber= 12
i=0
guessLimit= 3

while i<guessLimit:
    guess = int(input('Make a guess (1-20): '))
    i++
    if guess == secretNumber:
        print('You won')
        break
else:
    print('Sorry, you failed. Try again!')