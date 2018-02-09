#Make a two-player Rock-Paper-Scissors game.
#(Hint: Ask for player plays (using input), compare them, print out a
#message of congratulations to the winner, and ask if the players want to start a new game)

trigger = ""
while trigger != "end" or trigger != "end"  :
    player1 = input("Player 1, Rock(1), Paper(2) or Scissors(3)? ")
    player2 = input("Player 2, Rock(1), Paper(2) or Scissors(3)? ")

    if player1 == "rock" or player1 == "1":
        if player2 == "paper" or player2 == "2":
            print("Player 2 wins!")
            trigger = input("Press enter to continue playing or type 'end' to quit ")
        elif player2 == "scissors" or player2 == "3":
            print("Player 1 wins!")
            trigger = input("Press enter to continue playing or type 'end' to quit ")
        else:
            trigger = input("It is a tie! Press enter to continue playing or type 'end' to quit ")
    elif player1 == "paper" or player1 == "2":
        if player2 == "scissors" or player2 == "3":
            print("Player 2 wins!")
            trigger = input("Press enter to continue playing or type 'end' to quit ")
        elif player2 == "rock" or player2 == "1":
            print("Player 1 wins!")
            trigger = input("Press enter to continue playing or type 'end' to quit ")
        else:
            trigger = input("It is a tie! Press enter to continue playing or type 'end' to quit ")
    elif player1 == "scissors" or player1 == "3":
        if player2 == "paper" or player2 == "2":
            print("Player 1 wins!")
            trigger = input("Press enter to continue playing or type 'end' to quit ")
        elif player2 == "rock" or player2 == "1":
            print("Player 2 wins!")
            trigger = input("Press enter to continue playing or type 'end' to quit ")
        else:
            trigger = input("It is a tie! Press enter to continue playing or type 'end' to quit ")
    
