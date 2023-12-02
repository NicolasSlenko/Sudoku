import math, random, copy
class SudokuGenerator:
  '''
  create a sudoku board - initialize class variables and set up the 2D board
  This should initialize:
  self.row_length		- the length of each row
  self.removed_cells	- the total number of cells to be removed
  self.board			- a 2D list of ints to represent the board
  self.box_length		- the square root of row_length

  Parameters:
    row_length is the number of rows/columns of the board (always 9 for this project)
    removed_cells is an integer value - the number of cells to be removed

  Return:
  None
    '''
  #GOOD 
  def __init__(self, row_length, removed_cells):
    self.row_length = 9
    self.removed_cells = int(removed_cells)
    self.box_length = int(math.sqrt(self.row_length))
    self.board = [[0] * self.row_length for i in range(self.row_length)]
    '''''  
  Returns a 2D python list of numbers which represents the board

  Parameters: None
  Return: list[list]
    '''
  #GOOD 
  def get_board(self):
    return self.board

  '''
  Displays the board to the console
    This is not strictly required, but it may be useful for debugging purposes

  Parameters: None
  Return: None
    '''
  #GOOD 
  def print_board(self):
    for row in range(self.row_length):
      for col in range(self.row_length):
        print(f"{self.board[row][col]} ", end="")
      print()

  '''
  Determines if num is contained in the specified row (horizontal) of the board
    If num is already in the specified row, return False. Otherwise, return True

  Parameters:
  row is the index of the row we are checking
  num is the value we are looking for in the row

  Return: boolean
    '''
  #GOOD 
  def valid_in_row(self, row, num):
    for a in range(0, self.row_length):
      if self.board[row][a] == num:
        return False
    return True
    

  '''
  Determines if num is contained in the specified column (vertical) of the board
    If num is already in the specified col, return False. Otherwise, return True

  Parameters:
  col is the index of the column we are checking
  num is the value we are looking for in the column

  Return: boolean
    '''
  #GOOD 
  def valid_in_col(self, col, num):
    for a in range(0, self.row_length):
      if self.board[int(a)][int(col)] == num:
        return False
    return True

  '''
  Determines if num is contained in the 3x3 box specified on the board
    If num is in the specified box starting at (row_start, col_start), return False.
    Otherwise, return True

  Parameters:
  row_start and col_start are the starting indices of the box to check
  i.e. the box is from (row_start, col_start) to (row_start+2, col_start+2)
  num is the value we are looking for in the box

  Return: boolean
    '''
  #GOOD 
  def valid_in_box(self, row_start, col_start, num):
    for a in range(row_start, row_start + 3):
      for b in range(int(col_start), int(col_start + 3)):
        if 0 <= a < self.row_length and 0 <= b < self.row_length and self.board[
            a][b] == num:
          return False
    return True

  '''
    Determines if it is valid to enter num at (row, col) in the board
    This is done by checking that num is unused in the appropriate, row, column, and box

  Parameters:
  row and col are the row index and col index of the cell to check in the board
  num is the value to test if it is safe to enter in this cell

  Return: boolean
    '''
  #EDIT THIS ONE 
  def is_valid(self, row, col, num):
    
    if self.valid_in_row(row, num) and self.valid_in_col(col, num) and self.valid_in_box(row - row % int(self.box_length), col - col % int(self.box_length), num):
        return True
    return False


  '''
    Fills the specified 3x3 box with values
    For each position, generates a random digit which has not yet been used in the box

  Parameters:
  row_start and col_start are the starting indices of the box to check
  i.e. the box is from (row_start, col_start) to (row_start+2, col_start+2)

  Return: None
    '''
  #EDIT THIS ONE 
  def fill_box(self, row_start, col_start):
    # Fills the specified 3x3 box with values
    numbers = random.sample(range(1, self.row_length + 1), self.row_length)
    index = 0
    for a in range(row_start, row_start + 3):
      for b in range(col_start, col_start + 3):
          self.board[a][b] = numbers[index]
          index += 1

  '''
    Fills the three boxes along the main diagonal of the board
    These are the boxes which start at (0,0), (3,3), and (6,6)

  Parameters: None
  Return: None
    '''
  #good 
  def fill_diagonal(self):
    for start in range(0, int(self.row_length), 3):  # Cast to int here
        self.fill_box(int(start), int(start))
    #print("Board after filling diagonals:")
    #self.print_board()

  #good 
  def fill_remaining(self, row, col):
    if (col >= self.row_length and row < self.row_length - 1):
      row += 1
      col = 0
    if row >= self.row_length and col >= self.row_length:
      return True
    if row < int(self.box_length):
      if col < int(self.box_length):
        col = int(self.box_length)
    elif row < self.row_length - int(self.box_length):
      if col == int(row // self.box_length * self.box_length):
        col += int(self.box_length)
    else:
      if col == self.row_length - int(self.box_length):
        row += 1
        col = 0
        if row >= self.row_length:
          return True

    for num in range(1, self.row_length + 1):
      if self.is_valid(row, col, num):
        self.board[int(row)][int(
            col)] = num  
        if self.fill_remaining(int(row),
                               int(col) +
                               1):  
          return True
        self.board[int(row)][int(col)] = 0  
    return False

  #good 
  def fill_values(self):
    self.fill_diagonal()
    self.fill_remaining(0, self.box_length)

  #good 
  def remove_cells(self):
    cells_to_remove = self.removed_cells
    num_coords = 0
    while num_coords < self.removed_cells:
      row = random.randint(0, self.row_length - 1)
      col = random.randint(0, self.row_length - 1)
      if self.board[row][col] != 0:
        self.board[row][col] = 0
        num_coords += 1
        cells_to_remove -= 1
        if cells_to_remove == 0:
          return

#good
def generate_sudoku(size, removed):
  sudoku = SudokuGenerator(size, removed)
  sudoku.fill_values()
  board = sudoku.get_board()
  completed_board = copy.deepcopy(board)
  sudoku.remove_cells()
  board = sudoku.get_board()
  return board, completed_board


