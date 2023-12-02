from sudoku_generator import SudokuGenerator, generate_sudoku
from cell import Cell 

#check if board is solved 
def solved(board):
  for i in range(len(board)):
    for j in range(len(board)):
      if board[i][j] == 0:
        return False
  return True 

def print_board(board,row_length,col_length):
  for row in range(row_length):
    for col in range(row_length):
      print(f"{board[row][col]} ", end="")
    print()
    
# get input from UI to collect difficulty. Change with UI later
difficulty = input("Enter difficulty (easy, medium, hard): ")

if difficulty == "easy":
    numRemoved = 30
elif difficulty == "medium":
    numRemoved = 40
elif difficulty == "secret":
    numRemoved = 1
else:
    numRemoved = 50
game_board, solved_board = generate_sudoku(9, numRemoved)
print("Solved: ")
print_board(solved_board,9,9)

print("Player Board: ")
for a in range(0, len(game_board)):
  for b in range(0, len(game_board[a])):
    print(game_board[a][b], end = ' ')
  print()

'''
#Run the game (REPLIT LOGIC)
while not(solved(game_board)): 
  row = int(input("Enter row to enter: ")) - 1
  col = int(input("Enter column to enter: ")) - 1
  guess = int(input("Enter number guess 1-9: ")) 
  
  if(game_board[row][col] == 0):
    game_board[row][col] = guess
    print_board(game_board,9,9) 
    continue
  else:
    print("Can't edit a filled in cell!")
    continue
    

else:
  if game_board == solved_board:
    print("You Win!")
  else:
    print("You Lose!")
'''
  
#Play the game (PYGAME LOGIC)
x,y = 101,200 #input from clicking ex: (56, 49)
row = 1
col = 1 
cells = [] #cell[0] = cell1: row: 0, col: 0, etc. #So cell number = N - 1 

#create cells 
for i in range(0,9):
  for j in range(0,9):
    cells.append(Cell(i,j,game_board[i][j]))


    
#check which cell to access: returns index 
def returnCell(cells, row, col):
  for cell in cells:
      if cell.row == row and cell.col == col:
          return cell
  return None


#this would in in while loop 
currentCell = returnCell(cells,row,col)
if currentCell is not None:
  print(type(currentCell))
else:
  print("Cell not found")



  



  
  








