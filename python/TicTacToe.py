b = [
  [" ", " ", " "],
  [" ", " ", " "],
  [" ", " ", " "],
]

name   = input("What is your name? ")
print("Welcome to Tic Tac Toe, " + name + ". Here is our playing board:")

print(f"""
  1   2   3
1 {b[0][0]} | {b[0][1]} | {b[0][2]}
 --- --- ---
2 {b[1][0]} | {b[1][1]} | {b[1][2]}
 --- --- ---
3 {b[2][0]} | {b[2][1]} | {b[2][2]}
""")

player = "X"

# Loop for each turn
while True:
  print("It's " + player + "'s turn")
  position = input("Enter a position (i.e., 1,1): ")
  
  #Check the position is valid
  valid = position[0].isnumeric() and position[1] == "," and position[2].isnumeric()
  
  if valid:
    row = int(position[0])
    col = int(position[2])
  else:
    print("invalid position")
    continue
  
  # Update the board
  if (b[row - 1][col - 1] != " "):
    print("Position is occupied!")
    continue
  else:
    b[row - 1][col - 1] = player

  # display the board
  print(f"""
  1   2   3
1 {b[0][0]} | {b[0][1]} | {b[0][2]}
 --- --- ---
2 {b[1][0]} | {b[1][1]} | {b[1][2]}
 --- --- ---
3 {b[2][0]} | {b[2][1]} | {b[2][2]}
""")

  # Check win conditions
  # rows  
  for row in b:
    if row[0] == player and row[1] == player and row[2] == player:
      print("The winner is " + player)
      exit(0)
  # columns
  for i in range(0,3):
    if b[0][i] == player and b[1][i] == player and b[2][i] == player:
      print("The winner is " + player)
      exit(0)
  
  # diagonals
  if b[0][0] == player and b [1][1] == player and b[2][2] == player:
    print("The winner is " + player)
    exit(0)
  
  if b[2][0] == player and b [1][1] == player and b[0][2] == player:
    print("The winner is " + player)
    exit(0)

    for i in range(0,3):
      if (b[0][i] != "" and b[1][i] != "" and b[2][i] != ""):
        pass
      print("Board is full, Draw!")
      exit(0)
      
  
  # Update Player
  if player == "X":
    player = "O"
  else:
    player = "X"

