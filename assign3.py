#----------------------------------------------
#Name: Hayden Bridges
#Date: 02/02/16
#Assignment: 3
#Instructor: Sylvia Barnai
#----------------------------------------------

#begin program 1

number = 10                                                                             #the correct answer is 10

name = input("What is your name?: ")                                                    #prompt for user's name

for numAttempts in range (3):                                                           #set loop 3 times
    guess = input("Guess a number between 1 and 20: ")                                  #accept number value between 1 and 20
    guessInt = int(guess)                                                               #convert input into integer
    if (guessInt == number):                                                            #if the user guesses the number, breaks the loop and prints the number of guesses
        print("You are correct and you guessed it in %i attempt(s)" %(numAttempts+1))
        break
    elif (guessInt > number):                                                           #repeats the loop if the guess is too high
        print("Your guess is too high. Try again.")
    else:
        print("Your guess is too low. Try again.")                                      #repeats the loop if the guess is too low
    if (numAttempts == 2):                                                              #terminates the program if 3 guesses are exceeded
        print("Your three guesses are over, the number I was thinking of was 10.")

#end program 1

        
#begin program 2
def rps_decide(choice1, choice2):                                                                                           #define the choices
    if (choice1 == "p" and choice2 == "r") or (choice1 == "r" and choice2 == "s") or (choice1 == "s" and choice2 == "p"):   #create instances when player 1 wins
        return 1                                                                                                            #boolean value 1
    elif (choice1 == choice2):                                                                                              #if both players choose the same thing, then it's a draw
        return 0                                                                                                            #boolean value 0
    else:                                                                                                                   #player 2 is the winner
        return 2                                                                                                            #boolean value 2

for i in range(1):
    p1_choice = input("[R]ock, [P]aper, [S]cissors, shoot!: ").lower()                                                      #collects player 1's input and converts it into lower case
    p2_choice = input("[R]ock, [P]aper, [S]cissors, shoot!: ").lower()                                                      #collects player 2' input and converts it into lower case
    decision = rps_decide (p1_choice, p2_choice)                                                                            #allows the data to be collected once
    if decision == 1:                                                                                                       #recalls data from first function:
        print("Player 1 wins")                                                                                                  #boolean value 1 means player 1 wins
    elif decision == 2:                                                                                                         #boolean value 2 means player 2 wins
        print("Player 2 wins")
    else:                                                                                                                       #otherwise it's a draw
        print("It's a draw!")

#end program 2
