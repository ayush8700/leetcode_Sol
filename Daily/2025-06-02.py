# 135. Candy
# Hard

# Problem:
# There are n children standing in a line. Each child is assigned a rating value in the array `ratings`.
# You need to distribute candies to the children such that:
#   1. Each child must have at least one candy.
#   2. Children with a higher rating than their immediate neighbors must get more candies.
# Return the **minimum** number of candies you need to distribute to meet these rules.

# Example 1:
# Input: ratings = [1, 0, 2]
# Output: 5
# Explanation: Allocate candies as [2, 1, 2]

# Example 2:
# Input: ratings = [1, 2, 2]
# Output: 4
# Explanation: Allocate candies as [1, 2, 1]

# Constraints:
# - 1 <= ratings.length <= 2 * 10^4
# - 0 <= ratings[i] <= 2 * 10^4

class Solution:
    def candy(self, ratings: List[int]) -> int:
        N = len(ratings)
        
        # Step 1: Initialize each child with at least 1 candy
        candies = [1] * N

        # Step 2: Left to Right pass
        # Ensure that each child has more candies than the left neighbor if their rating is higher
        for i in range(1, N):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        # Step 3: Right to Left pass
        # Ensure the right neighbor rule: if ratings[i] > ratings[i+1], update accordingly
        for i in range(N - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                # Take the max because the left-to-right pass may have already assigned a higher value
                candies[i] = max(candies[i], candies[i + 1] + 1)

        # Step 4: Return the total number of candies needed
        return sum(candies)
