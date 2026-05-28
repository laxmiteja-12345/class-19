import random
playing=True
number=str(random.randint(0,9))
print("Guess a number to match with the number of system")
while playing:
    guess=int(input("Guess a number : "))
    if number==guess:
        print("You won the game!")
        print("The number was: ",number)
        break
    else:
        print("Your guess is incorrect, try again")

        
        






    
