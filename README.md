# Sudoku-Solver
A python sudoku solver using backtracking algorithm built with Numpy

How To Run:
1. Clone the repository
2. Install Numpy via windows terminal
3. Run Sudoku_Solver.py
4. Input each row of the puzzle as 9 numbers separated by space (0's to be filled in empty spaces)

How it Works
The code utilizes a recursive algorithm which...
1. Identifies an empty space
2. Tries inputting number from 1 - 9 
3. Determines if the position of the number is valid with respect to sudoku rules
4. If valid, then the algorithm repeats itself until all blank spaces are filled
5. If no number fits, the algorithm backtracks to the previous empty space it filled and inputs a different valid number
6. This is repeated until all spaces are filled
