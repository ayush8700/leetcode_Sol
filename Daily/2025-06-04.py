# 3403. Find the Lexicographically Largest String From the Box I
# Medium

# Problem:
# You are given a string `word`, and an integer `numFriends`.
# Alice splits the word into `numFriends` non-empty parts in every round of the game.
# All possible unique splits are used (i.e., no repeated way of splitting).
# All split strings are put into a box.
# 
# You must return the **lexicographically largest string** from all the strings in the box.

# Example 1:
# Input:
#   word = "dbca"
#   numFriends = 2
# Output: "dbc"
# Explanation:
#   Possible splits:
#     - "d", "bca" → "d", "bca"
#     - "db", "ca" → "db", "ca"
#     - "dbc", "a" → "dbc", "a"
#   The largest string is "dbc"

# Example 2:
# Input:
#   word = "gggg"
#   numFriends = 4
# Output: "g"
# Explanation:
#   The only valid split is: "g", "g", "g", "g"
#   So the answer is "g"

# Constraints:
# - 1 <= word.length <= 5000
# - word consists only of lowercase English letters.
# - 1 <= numFriends <= word.length

class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        # If there's only 1 friend, return the entire word
        if numFriends == 1:
            return word
        
        res = ''
        # The maximum length a substring can have in a split of `numFriends` parts
        length = len(word) - numFriends + 1

        for i in range(len(word) - length + 1):
            # Extract the candidate substring of length `length`
            temp = word[i:i + length]
            # Update result if this is lexicographically larger
            if temp > res:
                res = temp

        return res
