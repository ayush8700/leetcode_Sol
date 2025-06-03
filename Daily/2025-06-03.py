# 1298. Maximum Candies You Can Get from Boxes
# Hard

# Problem:
# You are given `n` boxes labeled from 0 to n - 1. Each box may be:
# - Open or closed (status[i] == 1 means open)
# - Contain a number of candies (candies[i])
# - Contain keys to other boxes (keys[i])
# - Contain other boxes (containedBoxes[i])

# You are given some boxes initially (initialBoxes).
# You can only open a box if it's open (status[i] == 1) or if you obtain its key from another box.
# You can also explore the boxes found inside other boxes you open.

# Goal:
# Return the **maximum number of candies** you can collect by following the rules above.

# Example 1:
# Input:
#   status = [1,0,1,0]
#   candies = [7,5,4,100]
#   keys = [[],[],[1],[]]
#   containedBoxes = [[1,2],[3],[],[]]
#   initialBoxes = [0]
# Output: 16
# Explanation:
#   Open box 0 (it's open), get 7 candies, find boxes 1 and 2
#   Box 2 is open → open and get 4 candies and key to box 1
#   Now you can open box 1 → get 5 candies and find box 3 (but no key to 3)
#   Total: 7 + 4 + 5 = 16

# Constraints:
# - 1 <= n <= 1000
# - All arrays have length n
# - candies[i] ∈ [1, 1000]
# - All values in keys[i] and containedBoxes[i] are unique

class Solution:
    def maxCandies(self, status: List[int], 
                   candies: List[int], 
                   keys: List[List[int]], 
                   containedBoxes: List[List[int]], 
                   initialBoxes: List[int]) -> int:
        
        foundOpenable = True  # Flag to check if progress is made in each iteration
        totalCandies = 0      # Track total candies collected

        while initialBoxes and foundOpenable:
            foundOpenable = False
            nextBoxes = []

            for boxId in initialBoxes:
                if status[boxId]:  # If the box is open
                    foundOpenable = True
                    totalCandies += candies[boxId]  # Collect candies

                    # Collect any boxes found inside this box
                    nextBoxes.extend(containedBoxes[boxId])

                    # Use keys found to unlock other boxes
                    for keyId in keys[boxId]:
                        status[keyId] = 1
                else:
                    # Can't open this box yet, keep it for the next round
                    nextBoxes.append(boxId)

            initialBoxes = nextBoxes  # Update the list for the next iteration

        return totalCandies
