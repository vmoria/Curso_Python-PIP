import random # Import the random module

def Choose_Options():
  Options = ("ROCK", "PAPER", "SCISSOR") # Tuple - Local Scope
  User_Option = input("Type ROCK, PAPER or SCISSOR => ") # Local Scope
  User_Option = User_Option.upper()

  if not User_Option in Options:
    print("Invalid option")
    # continue # It continues the loop, if the user types an invalid option the loop reestart again
  # Computer_Option = "ROCK"
    return None, None
    
  Computer_Option = random.choice(Options) # Local Scope

  print('User option =>', User_Option)
  print('Computer option =>', Computer_Option)
  return User_Option, Computer_Option

def Check_Rules(User_Option, Computer_Option, User_Wins, Computer_Wins):
  if User_Option == Computer_Option:
    print ("Tie!, you both chose the same option")
  elif User_Option == "ROCK":
    if Computer_Option == "SCISSOR":
      print("Rock beats scissor, you win!")
      User_Wins += 1
    else:
      print("Paper beats rock, you lose!")
      Computer_Wins += 1
  elif User_Option == "PAPER":
    if Computer_Option == "ROCK":
      print ("Paper beats rock, you win!")
      User_Wins += 1
    else:
      print("Scissor beats paper, you lose!")
      Computer_Wins += 1
  elif User_Option == "SCISSOR":
    if Computer_Option == "PAPER":
      print("Scissor beats paper, you win!")
      User_Wins += 1
    else:
      print("Rock beats scissor, you lose!")
      Computer_Wins += 1
  return User_Wins, Computer_Wins

def Check_Winner(User_Wins, Computer_Wins):
  if Computer_Wins == 2:
    print("The computer has won the match")
    exit() # It stops the program - Instead of BREAK
  if User_Wins == 2:
    print("The user has won the match")
    exit() # It stops the program - Instead of BREAK
  return User_Wins, Computer_Wins

def Run_Game():
  Computer_Wins = 0
  User_Wins = 0
  Rounds = 1
  while True:
    print("*" * 10)  # Print 10 times the *
    print("ROUND", Rounds)
    print("*" * 10)
    print("Computer Wins", Computer_Wins)
    print("User Wins", User_Wins)
    Rounds += 1
  
    User_Option, Computer_Option = Choose_Options() # Tuple - What the Function returns
    User_Wins, Computer_Wins = Check_Rules(User_Option, Computer_Option, User_Wins, Computer_Wins)
    User_Wins, Computer_Wins = Check_Winner(User_Wins, Computer_Wins)

Run_Game()