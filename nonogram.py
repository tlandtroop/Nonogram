def initialize_board():
    board = []
    for i in range(5):
        row = []
        for j in range(5):
            row.append("-")
        board.append(row)
    return board

def mark_square(board, row, col, mark):
  if mark == "Mark":
    board[row][col] = '1'
  elif mark == "Unmark":
    board[row][col] = '0'
  elif mark == "Flag":
    board[row][col] = '2'

def print_board(board):
  for i, row in enumerate(board):
    for j, col in enumerate(row):
      print(board[i][j], end=" ")
    print()  

def is_valid(board, row, col):
    if 0 <= row <= (5-1) and 0 <= col <= (5-1):
        return True
    return False
