#Lam Manning 10-24-23

#function
def nameGen(): #Plays the Name Game.
    print("Welcome to Your Breaking Bad Character Name")
    print("Answer the questions to find out your character name")
    ans = input("Hello Kitty (h) or Kuromi (k)? ")
    if ans =="h":
        ans = input("Opera (o) or Kpop (k)? ")
        if ans == "o":
            ans = input("Cookies (co) or Cake (ca)? ")
            if ans == "co":
                print("You are Walter White")
            elif ans =="ca":
                print("Your name is Marie Schrader")
            else:
                print("Invalid! Please type (co) or (ca). ")
                nameGen()
        elif ans=="k":
            ans = input("Ice Cream (i) or Pizza (p)? ")
            if ans =="i":
                print("Your Name is Saul Goodman.")
            elif ans=="p":
                print("Your name is Jesse Pinkman, yo!")
            else:
                print("Invalid! Please type (i) or (p). START OVER")
                nameGen()
        else:
            print("Invalid! Please type (o) or (k). START OVER ")
            nameGen()
    elif ans== "k":
        ans = input("Rock (ro) or Rap (ra)? ")
        if ans == "ro":
            ans = input ("Chicken (c) or Beef (b)? ")
            if ans == "c":
                print("Your name is Gus Fring")
            elif ans=="b":
                print("Your Name is Mike Ehrmantraut")
            else:
                print("Invalid! Please type (c) or (b). START OVER")
                nameGen()
        else:
            ans = input("Soup (s) or Nachos (n)? ")
            if ans =="s":
                print("Your name is Skylar White. (yo!)")
            elif ans =="n":
                print("Your Name is Hank Schrader.")
            else:
                print("Invalid! Please type (s) or (n). START OVER")
                nameGen()
    else:
        print("Invalid! Please type (h) or (k). START OVER")
        nameGen()
#main
nameGen()
ans = input("Want to Play Again? (Yes/No) " )
if ans == "Yes":
    nameGen()
elif ans =="No":
    print("Goodbye!")
else:
    print("Invalid Answer. Please type: Yes or No!")
    ans = input("Want to Play Again? (Yes/No) " )

