#Text based Rock Paper Scissors
import random

def lineBreaks():
    print("---")

print("Welcome to Text Based Rock Paper Scissors")
lineBreaks()
print("To start off , enter your name below")
lineBreaks()

#Input Player Name
player1 = input("Please Enter your name ---Player 1 is : ")
lineBreaks()
player2 = "The Computer"
print("Player 2 is" ,player2)
#Input 0,1 or 2
lineBreaks()
x = input("Enter 0 for rock,1 for paper,2 for scissors : ")
p1 = int(x)
#Generating random input for player 2
p2 = random.randint(0,2)

	
#Assigning 0,1,2 to Rock,Paper,Scissors
def assign():
	if p1 == 0:
		print(player1 ,"chose rock")
	if p1 == 1:
		print(player1 , "chose paper")
	if p1 == 2:
		print(player1 ,"chose scissors")
	if p2 == 0:
		print(player2,"chose rock")	
	if p2 == 1:
		print(player2,"chose paper")
	if p2 == 2:
		print(player2, "chose scissors")			

	
#Defining the rules of Rock,Paper,Scissors
def rules():
	if p1 == p2:
		print("Match Drawn")
	if 	p1 == 0  and p2 == 1: #rock paper
		print( player2,"wins")
	if p1 == 0 and p2 == 2: #rock scissors
		print(player1, "wins")
	if p1 == 1 and p2 == 0: #paper rock
		print(player1, "wins")
	if p1 == 1 and p2 ==2:  #paper scissors
		print(player2," wins")
	if p1 == 2 and p2 == 0:
		print(player2," wins")	# scissors rock
	if p1 == 2 and p2 == 1:
		print(player1," wins")	#scissors paper


assign()
rules()		

lineBreaks()
print("To play again,press ctrl+F5")	
lineBreaks()
print("Created By Yahya Khan")
lineBreaks()	

	

	





