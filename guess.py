import random
print('This program will ask you to guess the number between 1 and 20')
print('Try to do it in as few guesses as possible!')
number = random.randint(1,21)
for guessesTaken in range(1,7):
    print('Your guess?')
    guess = int(input())
    
    if (guess < number):
        print ('Your guess is too low')
    elif (guess > number):
        print ('Your guess is too high')
    else:
        break    

if (guess == number):
    print('Good job! You guessed the number in ' + str(guessesTaken) + ' guesses!')
else:
    print('No luck! The number I was thinking of was ' + str(number))
