'''
Flores Esquivel Luis Antonio
Teoria de la Computacion 5BM1
Automata finito no determinista - Tablero
30/09/2023
'''

from board_classes import Square


# First we have to create the board, it will be a 4 x 4 squares board


board_rows = 4
board_columns = 4


def create_board(board_rows, board_columns):
    '''
    Create a board compound with squares, each square has a colour, value and a pair of coordinates.
    '''
    
    board = [[None] * board_columns  for _ in range(board_rows)] # Define the dimension of the board
    
    # Caculate the colour and numerical_value for each square and then 

    for i in range(board_rows):
        
        for j in range(board_columns):
            
            if (i + j) % 2 == 0:
                
                colour = 'B'
                
            else:
                
                colour = 'R'
            
            value = ((i) * 4) + (j + 1)
            new_square = Square(i, j, colour, value)
            
            board[i][j] = new_square
    
    return board


def define_neighbors(board, board_rows, board_columns):
    '''
    Define all the neighbors for each square in the board.
    '''
    
    for i in range(board_rows):
        
        for j in range(board_columns):
            
            actual_square = board[i][j] # Obtain the actual square
            
            neighbors = [] # Create a list to store all the neighbors
           
            for di in [-1, 0, 1]:
                for dj in [-1, 0, 1]:
                    new_square_i = i + di
                    new_square_j = j + dj
                    if 0 <= new_square_i < board_rows and 0 <= new_square_j < board_columns and (new_square_i != i or new_square_j != j):
                        neighbors.append(board[new_square_i][new_square_j])
            actual_square.neighbors = neighbors


def print_board(board):
    '''
    Print the board elements to see if it was created correctly.
    '''
    
    print("\nBoard representation with colours: \n")
    
    for row in board:
        for square in row:
            print(f"{square.colour}", end=' ')
        print()  # New line at the end of each row
        
    print("\nBoard representation with numerical_values: \n")
    
    for row in board:
        for square in row:
            print(f"{square.value}", end=' ')
        print()  # New line at the end of each row
        

    print("\nBoard squares and their neighbors: \n")
    
    for row in board:
        for square in row:
            for neighbor in square.neighbors:
                
                print("")
    
            

def main():
    
    board = create_board(board_rows, board_columns)
    
    define_neighbors(board, board_rows, board_columns)
    
    print_board(board)

    
    
if __name__ == "__main__":
    
    main()