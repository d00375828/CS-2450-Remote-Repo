import random

print('Hi I am going to guess your age!')
name = input('What is your name?')

#guesses = []
guessed = False
while(guessed == False):
    guess = random.randint(15,30)
    #if guess in guesses:
       # continue

    user_response = input("Are you "+str(guess)+ "years old?")
    if user_response == 'y' or user_response =='Y':
        print(f'Haha! {name} is ' + str(guess)+ 'years old! I guess it!')
        guessed == True
        break
    else:
        print('Rats')
        #guesses.append(guess)