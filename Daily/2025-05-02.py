# 838. Push Dominoes
# Medium

# There are n dominoes in a line. Initially, they are all standing vertically.
# Some dominoes are pushed to the left ('L') or to the right ('R') at time t = 0.
# Each second, a falling domino pushes the adjacent domino in its direction.

# If a domino is pushed simultaneously from both directions, it stays upright due to balanced forces.

# Input:
# - A string `dominoes` of length n
# - 'L' for pushed left, 'R' for pushed right, '.' for standing

# Output:
# - A string representing the final state of all dominoes.

# Example 1:
# Input: dominoes = "RR.L"
# Output: "RR.L"
# Explanation: No domino falls between the R and L due to equal opposing forces.

# Example 2:
# Input: dominoes = ".L.R...LR..L.."
# Output: "LL.RR.LLRRLL.."

# Constraints:
# n == dominoes.length
# 1 <= n <= 10^5
# dominoes[i] ∈ {'L', 'R', '.'}

class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        N = len(dominoes)
        forces = [0] * N  # To store net force on each domino
        
        force = 0
        # Left to right pass: apply positive force from 'R'
        for i in range(N):
            if dominoes[i] == 'R':
                force = N
            elif dominoes[i] == 'L':
                force = 0
            else:
                force = max(force - 1, 0)
            forces[i] += force

        force = 0
        # Right to left pass: apply negative force from 'L'
        for i in range(N - 1, -1, -1):
            if dominoes[i] == 'L':
                force = N
            elif dominoes[i] == 'R':
                force = 0
            else:
                force = max(force - 1, 0)
            forces[i] -= force

        # Build result based on net force
        result = []
        for f in forces:
            if f > 0:
                result.append('R')
            elif f < 0:
                result.append('L')
            else:
                result.append('.')

        return ''.join(result)
