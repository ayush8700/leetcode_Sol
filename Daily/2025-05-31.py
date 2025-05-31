# 909. Snakes and Ladders
# Medium

# You are given an n x n board representing a Snakes and Ladders game.
# The board is filled with integers:
# -1 indicates a normal square,
# any other value indicates the destination of a snake or ladder.

# The board is labeled from 1 to n^2 in a Boustrophedon style starting from the bottom-left.
# You start on square 1. Each move simulates rolling a die (1-6 steps).
# If you land on a ladder/snake, you move to its destination.
# You only follow one jump per dice roll, even if it lands on another ladder/snake.

# Return the least number of dice rolls to reach square n^2.
# If it's impossible, return -1.

# Example:
# Input: board = [[-1,-1,-1,-1,-1,-1],
#                 [-1,-1,-1,-1,-1,-1],
#                 [-1,-1,-1,-1,-1,-1],
#                 [-1,35,-1,-1,13,-1],
#                 [-1,-1,-1,-1,-1,-1],
#                 [-1,15,-1,-1,-1,-1]]
# Output: 4

from collections import deque

class Solution(object):
    def snakesAndLadders(self, board):
        n = len(board)
        
        # This array keeps track of the minimum number of dice rolls to reach each square
        min_rolls = [-1] * (n * n + 1)
        min_rolls[1] = 0  # Starting at square 1
        q = deque([1])    # BFS queue initialized with the starting square

        while q:
            x = q.popleft()  # Current square
            
            # Try all possible dice rolls (1 to 6)
            for i in range(1, 7):
                t = x + i  # Tentative next square
                if t > n * n:
                    break  # Skip if out of bounds

                # Convert 1D square number to 2D board coordinates
                row = (t - 1) // n
                col = (t - 1) % n

                # Adjust column based on row parity for boustrophedon pattern
                if row % 2 == 1:
                    col = n - 1 - col

                # Get the value at the board cell (snake, ladder or -1)
                val = board[n - 1 - row][col]  # Remember: board is from bottom to top

                # If there's a snake or ladder, move to its destination
                y = val if val != -1 else t

                # If we reach the last square, return the number of rolls taken
                if y == n * n:
                    return min_rolls[x] + 1

                # If this is the first time visiting this square
                if min_rolls[y] == -1:
                    min_rolls[y] = min_rolls[x] + 1
                    q.append(y)

        # If the last square was never reached
        return -1
