import random

magicNumber = random.randint(1, 100)

print("Bienvenue sur Magic Number ! J'ai choisi un chiffre entre 1 et 100, devine quel est mon chiffre !")


userNumber = input("Quel chiffre proposez-vous? ")
try:
    val = int(userNumber)
except ValueError:
    print("Ce n'est pas un chiffre! Merci de ré-essayer")
    userNumber = input("Quel chiffre proposez-vous? ")

while magicNumber != int(userNumber):
    if int(userNumber) > magicNumber:
        print("C'est trop grand ! Choisis un chiffre plus petit.")
        userNumber = input("Choisis un nouveau nombre : ")
        try:
            val = int(userNumber)
        except ValueError:
            print("Ce n'est pas un chiffre! Merci de ré-essayer")
            userNumber = input("Quel chiffre proposez-vous? ")
    elif int(userNumber) < magicNumber:
        print("C'est trop petit ! Choisis un chiffre plus grand.")
        userNumber = input("Choisis un nouveau nombre : ")
        try:
            val = int(userNumber)
        except ValueError:
            print("Ce n'est pas un chiffre! Merci de ré-essayer")
            userNumber = input("Quel chiffre proposez-vous? ")

print("Bravo tu as trouvé ! Le chiffre que j'avais choisi était le " + str(magicNumber))
