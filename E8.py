print("Welcome to rock, paper, scissors")
stop = input("Press enter to start")
while stop != "stop":
    player1,player2 = 0,0
    while player1 not in ("rock","paper","scissors"):
        player1 = str(input("Player one\nChoose your fighter: "))
    while player2 not in ("rock","paper","scissors"):
        player2= str(input("Player two \n Choose your fighter: "))
    if (player1 == "rock" and player2 == "scissors"
    or player1 == "paper" and player2 == "rock"
    or player1 == "scissors" and player2 == "paper"):
        print("Player One Wins")
    elif player1 == player2:
        print("Players have tied")
    else:
        print("Player Two Wins")
    stop = input("type \'stop\' to quit or press enter to replay: \n")
    
