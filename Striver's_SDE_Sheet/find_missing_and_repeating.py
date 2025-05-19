# find_missing_and_repeating.py

class Solution:
    def find_missing_and_repeating(self, arr):
        """
        Problem Statement:
        You are given a read-only array of N integers with values also in the range [1, N] both inclusive.
        Each integer appears exactly once except A which appears twice and B which is missing.
        The task is to find the repeating and missing numbers A and B where A repeats twice and B is missing.

        Parameters:
        arr (List[int]): List of integers of size N with values in range [1, N]

        Returns:
        List[int]: A list containing two elements [A, B], where A is the repeating number, and B is the missing number.

        Example 1:
        Input: arr = [3, 1, 2, 5, 3]
        Output: [3, 4]

        Example 2:
        Input: arr = [3, 1, 2, 5, 4, 6, 7, 5]
        Output: [5, 8]
        """
        # TODO: Implement this method

        N = len(arr)

        hash = [0] *(N+1)

        for i in range(N):
            hash[arr[i]] += 1

        repeating = -1
        missing = -1

        for i in range(N+1):
            if hash[i] == 0:
                missing = i
            if hash[i] == 2:
                repeating = i
        return ([repeating, missing])



if __name__ == "__main__":
    sol = Solution()

    # Test Case 1
    input1 = [3, 1, 2, 5, 3]
    expected1 = [3, 4]
    print("Input:", input1)
    print("Expected Output:", expected1)
    print("Your Output:", sol.find_missing_and_repeating(input1))
    print()

    # Test Case 2
    input2 = [3, 1, 2, 5, 4, 6, 7, 5]
    expected2 = [5, 8]
    print("Input:", input2)
    print("Expected Output:", expected2)
    print("Your Output:", sol.find_missing_and_repeating(input2))
    print()
