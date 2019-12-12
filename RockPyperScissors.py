import random 

choice = ["Rock", "Pyper", "Scissors"]
computerChoice = choice[random.randint(0, 2)]

playerScore = 0
computerScore = 0

print("Bienvenue à toi sur Rock, Pyper, Scissors ! Fais ton choix jeune voyageur :")

playerChoice = input("Rock, Pyper, Scissors ? ")

while playerScore != 10 or computerScore != 10:
    if playerChoice == computerChoice:
            print("Oh non ! C'est un égalité entre vous deux !")
            computerChoice = choice[random.randint(0, 2)]
            playerChoice = input("Rock, Pyper, Scissors ?")
    elif playerChoice == "Rock":
        if computerChoice == "Pyper":
            computerScore += 1
            print("Perdu !  Point pour l'ordinateur ! Il y actuellement " + str(computerScore) + " Points")
            print("Tu n'as que " + str(playerScore) + " Points")

            computerChoice = choice[random.randint(0, 2)]
            playerChoice = input("Rock, Pyper, Scissors ? ")
        elif computerChoice == "Scissors":
            playerScore += 1
            print("Gagné ! Point pour le joueur ! Tu as " + str(playerScore) + " Points")
            print("L'ordinateur n'a que " + str(computerScore) + "Points")

            computerChoice = choice[random.randint(0, 2)]
            playerChoice = input("Rock, Pyper, Scissors ? ")
    elif playerChoice == "Pyper":
        if computerChoice == "Scissors":
            computerScore += 1
            print("Perdu !  Point pour l'ordinateur ! Il y actuellement " + str(computerScore) + " Points")
            print("Tu n'as que " + str(playerScore) + " Points")

            computerChoice = choice[random.randint(0, 2)]
            playerChoice = input("Rock, Pyper, Scissors ? ")
        elif computerChoice == "Rock":
            playerScore += 1
            print("Gagné ! Point pour le joueur ! Tu as " + str(playerScore) + " Points")
            print("L'ordinateur n'a que " + str(computerScore) + "Points")

            computerChoice = choice[random.randint(0, 2)]
            playerChoice = input("Rock, Pyper, Scissors ? ")
    elif playerChoice == "Scissors":
            if computerChoice == "Rock":
                computerScore += 1
                print("Perdu !  Point pour l'ordinateur ! Il y actuellement " + str(computerScore) + " Points")
                print("Tu n'as que " + str(playerScore) + " Points")

                computerChoice = choice[random.randint(0, 2)]
                playerChoice = input("Rock, Pyper, Scissors ? ")
            elif computerChoice == "Pyper":
                playerScore += 1
                print("Gagné ! Point pour le joueur ! Tu as " + str(playerScore) + " Points")
                print("L'ordinateur n'a que " + str(computerScore) + "Points")

                computerChoice = choice[random.randint(0, 2)]
                playerChoice = input("Rock, Pyper, Scissors ? ")
    else:
        print("Je pense que tu as mal écris ton choix !")
        playerChoice = input("Rock, Pyper, Scissors ? ")

if computerScore == 10:
    print("Bah dis donc, tu n'es pas très fort ! L'ordinateur a gagné !")
elif playerScore == 10:
    print("Bravo tu as battu l'ordinateur ! Je savais que tu y arriverai !")