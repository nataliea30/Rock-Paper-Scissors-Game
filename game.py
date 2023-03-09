import random

#score
human_score = 0
computer_score = 0

#starts the game, allows player to input
while True:
  options = ["rock", "paper", "scissors"]
  ai = random.choice(options)
  player = None
  
  #only accepts rock, paper, scisscors (in any case) as an input, if else is inputed -> the player is prompted to input again
  while player not in options:
    player = input("Rock, paper, scissors, shoot! Which one do you choose?\n").lower()
    
  
  #codes the games mechanics, tells the results of the game, and adds to the score.
  if player == ai:
    print ("You: "+str(player))
    print ("Computer: "+str(ai))
    print ("It's a tie!")
    print ("Score: You: "+str(human_score)+"  Computer: "+str(computer_score))
  
  elif (player == "paper"):
    if ai == "rock":
      print ("You: "+str(player))
      print ("Computer: "+str(ai))
      print ("You win!")
      human_score += 1
      print ("Score: You: "+str(human_score)+"  Computer: "+str(computer_score))
    else: 
      print ("You: "+str(player))
      print ("Computer: "+str(ai))
      print ("Computer wins!")
      computer_score += 1
      print ("Score: You: "+str(human_score)+"  Computer: "+str(computer_score))
  
  elif player == "rock":
    if ai == "scissors":
      print ("You: "+str(player))
      print ("Computer: "+str(ai))
      print ("You win!")
      human_score += 1
      print ("Score: You: "+str(human_score)+"  Computer: "+str(computer_score))
    else: 
      print ("You: "+str(player))
      print ("Computer: "+str(ai))
      print ("Computer wins!")
      computer_score += 1
      print ("Score: You: "+str(human_score)+"  Computer: "+str(computer_score))
  
  elif player == "scissors":
    if ai == "paper":
      print ("You: "+str(player))
      print ("Computer: "+str(ai))
      print ("You win!")
      human_score += 1
      print ("Score: You: "+str(human_score)+"  Computer: "+str(computer_score))
    else: 
      print ("You: "+str(player))
      print ("Computer: "+str(ai))
      print ("Computer wins!")
      computer_score += 1
      print ("Score: You: "+str(human_score)+" Computer: "+str(computer_score))
  

#asks the player if they would like to play again, the score remains from the last game if yes is hit and continues.
  play = input("Would you like to play again? Enter (y/n) ")
  if play != (("y") or ("Y")):
    break

#if the player says anything else besides y, the game will end and the score will be prompted.
print ("Thank you for playing! (: \nFinal Score: You: "+str(human_score)+"  Computer: "+str(computer_score))
    



  
