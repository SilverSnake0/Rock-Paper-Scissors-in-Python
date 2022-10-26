import random
#function to make sure the user choice is one of the possible  options
def getUserChoice(choice):
    choices = ['rock', 'paper', 'scissors', 'bomb']
    for i in choices:
        if choice == i:
            return choice
        else:
            print("Error: This is not a valid option. Choices are Rock, Paper, or Scissors.")
#function to obtain the computer choice randomly from the three possible choices
def getComputerChoice():
    compChoice = ['rock', 'paper', 'scissors']
    computerChoice = random.choice(compChoice)
    return computerChoice
#function to determine who will win out of the possible outcomes
def determineWinner(userChoice, computerChoice):
    if userChoice == computerChoice:
        return 'The game was a tie!'
    elif userChoice == 'bomb':
        return 'You have won the game! :)'
    elif userChoice == 'rock' and computerChoice =='scissors':
        return 'You have won the game! :)'
    elif userChoice == 'paper' and computerChoice =='rock':
        return 'You have won the game! :)'
    elif userChoice == 'scissors' and computerChoice =='paper':
        return 'You have won the game! :)'
    else:
        return 'The computer has won the game :('
#function to utilize the earlier functions and find the winner
def playGame(userChoice):
    userChoice = getUserChoice(userChoice)
    computerChoice = getComputerChoice()
    print(f'User played: {userChoice}.\n Computer played: {computerChoice}.\n {determineWinner(userChoice, computerChoice)}')

playGame('bomb')