print("Welcome to Mustang Bucks!!! The game where you can win a Ford Mustang or Ford Bucks!!")
print("Directions:")
print("Win a 2027 Ford Mustang Mach E, by entering the winning numbers for each round. You must win all three rounds to win your Ford 2027 Mustang Mach E.")
print("Battery Dying, from losing rounds one and/or two?! Charge up and Hit the Road, AGAIN!! You can WIN $200 FORD BUCKS by ONLY matching the winning numbers in round three!!")
print("Will you win a Ford Mustang or Ford Bucks?")
print("Push to Start and Buckle Up....")
winningNumber1 = 301
winningNumber2 = 954
winningNumber3 = 404

guess1 = int(input("Enter Three numbers:"))
if guess1 == winningNumber1:
        print("YOU ENTERED THE WINNING NUMBERS!!! Congratulations!! If you win in round two, you're closer to owning a 2027 Ford Mustang Mach E!!")
else:
    print("Wrong Turn! Keep playing to Win $200 in Ford Bucks!") 
    
guess2 = int(input("Enter Three numbers:"))
if guess2 == winningNumber2:
    print("YOU ENTERED THE WINNING NUMBERS!!! Congratulations!! You're one round away from owning a 2027 Ford Mustang Mach E!! Let's play!")
else:
    print("Avoid A Crash...Watch for hazards on the road!")
    print("Play Again to WIN $200 in Ford Bucks!")
    
guess3 = int(input("Enter Three numbers:"))
if guess3 == winningNumber3: 
    print("YOU WON $200 in Ford Bucks. Print this ticket and CASH OUT at a Ford dealership! Thanks for playing!, Mustang Bucks!")
else:
    print("You Crashed OUT! Play Again?")
