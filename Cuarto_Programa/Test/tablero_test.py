# '''
# Flores Esquivel Luis Antonio
# Teoria de la Computacion 5BM1
# Automata finito no determinista - Tablero
# 30/09/2023
# '''

# # We begin with the chess board declaration

# board = [
    
#     ('B', 'R', 'B', 'R'),
#     ('R', 'B', 'R', 'B'),
#     ('B', 'R', 'B', 'R'),
#     ('R', 'B', 'R', 'B')
    
# ]


# def enum_squares(board_matrix):
    
#     '''
#     Function where we assing a numerical value for each square on the board.
#     The squares takes values from 1 - 16.
#     '''
    
#     # First we obtain the rows and columns of the board_matrix
    
#     rows_board = len(board_matrix)
    
#     columns_board = len(board_matrix[0])
    
    
#     print("Rows: " + str(rows_board))
#     print("Columns: " + str(columns_board))
    
#     # Create a dictionary to save each square and their value
    
#     square_values = {}
    
#     for row in range(rows_board):
#         for column in range(columns_board):
#             numerical_value = (row * rows_board) + (column + 1)
#             square_values[(row, column)] = numerical_value    
    
#     print(square_values)
    

# def obtain_numerical_value(x_square, y_square, squares_values):
    
#     '''
#     Each square from the board, has a numerical value stored in a dictionary.
#     '''
    
#     numerical_value = squares_values[(x_square, y_square)]
    
#     return numerical_value
    
    
    
    
# def obtain_neighbors(x_square, y_square):
    
#     '''
#     With the x and y component of the square we can obtain the neighbors.
#     '''
    
#     neigbors = []
    
#     coordinates_neighbors = [(x_square-1, y_square), (x_square+1, y_square), (x_square, y_square-1), (x_square, y_square+1)]
    
#     for 
    
    
    
    
    
# def main():
    
#     enum_squares(board)


# if __name__ == "__main__":
    
#     main()