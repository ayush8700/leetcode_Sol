# 3335. Total Characters in String After Transformations I
#
# Given a string `s` and an integer `t`, return the length of the string
# after performing `t` transformations where:
# - Each character becomes the next letter (e.g., 'a' -> 'b', ..., 'y' -> 'z')
# - If a character is 'z', it becomes the string "ab"
#
# Return the final length of the string after t transformations, modulo 10^9 + 7.
#
# Example:
# Input: s = "abcyy", t = 2
# Output: 7
# Explanation:
#   After 1st transformation: "bcdzz"
#   After 2nd transformation: "cdeabab" → length is 7
#
# Constraints:
# - 1 <= s.length <= 10^5
# - s consists of lowercase English letters
# - 1 <= t <= 10^5

# SOLUTION

class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        Mod = 10 ** 9 +7

        count =[0] * 26

        for char in s:
            count [ord(char)- ord('a')] += 1
        
        for i in range(t):
            newCount = [0] * 26

            for j in range(len(newCount)):
                if j == 25:
                    newCount[0] += count[j]
                    newCount[1] += count[j]

                else:
                    newCount[j+1] += count[j]
            count = newCount
        return sum(count) % Mod


         
                

        


