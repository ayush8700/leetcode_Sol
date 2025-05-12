# 2094. Finding 3-Digit Even Numbers
#
# Given a list of digits, return all unique 3-digit even numbers that:
# - Have no leading zero
# - Use digits from the input (no more than their frequency)
# - Are even
#
# Example:
# Input: digits = [2,1,3,0]
# Output: [102,120,130,132,210,230,302,310,312,320]

class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        N = len(digits)
        total = set()
        for i in range(N):
            for j in range(N):
                for k in range(N):
                    if i ==j or i==k or j==k:
                        continue
                    nums = digits[i]*100 + digits[j]*10 +digits[k]
                    if nums %2 == 0 and nums >= 100:
                        total.add(nums)
        return sorted(list(total))
                    



        
