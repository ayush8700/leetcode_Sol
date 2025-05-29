# count_inversions.py

from typing import List

class Solution:
    def countInversions(self, arr: List[int]) -> int:
        """
        Problem Statement:
        Given an array of N integers, count the number of inversions in the array using merge-sort.

        Definition: An inversion is a pair (A[i], A[j]) such that i < j and A[i] > A[j].

        Parameters:
        arr (List[int]): The input array.

        Returns:
        int: Total number of inversions in the array.

        Example 1:
        Input: arr = [1, 2, 3, 4, 5]
        Output: 0

        Example 2:
        Input: arr = [5, 4, 3, 2, 1]
        Output: 10

        Example 3:
        Input: arr = [5, 3, 2, 1, 4]
        Output: 7
        """
        # TODO: Implement this method using merge sort                
        def merge_sort(start, end):
            if start >= end:
                return 0

            mid = (start + end) // 2
            count = merge_sort(start, mid) + merge_sort(mid + 1, end)

            # Merge step and count inversions
            temp = []
            left, right = start, mid + 1

            while left <= mid and right <= end:
                if arr[left] <= arr[right]:
                    temp.append(arr[left])
                    left += 1
                else:
                    temp.append(arr[right])
                    count += (mid - left + 1)  # All elements from left to mid are greater
                    right += 1

            while left <= mid:
                temp.append(arr[left])
                left += 1
            while right <= end:
                temp.append(arr[right])
                right += 1

            for i in range(len(temp)):
                arr[start + i] = temp[i]

            return count

        return merge_sort(0, len(arr) - 1)
        pass


        



def run_tests():
    sol = Solution()
    
    test_cases = [
        ([1, 2, 3, 4, 5], 0),
        ([5, 4, 3, 2, 1], 10),
        ([5, 3, 2, 1, 4], 7),
        ([2, 4, 1, 3, 5], 3),
        ([10, 10, 10], 0),
    ]

    for i, (arr, expected) in enumerate(test_cases, 1):
        result = sol.countInversions(arr)
        print(f"Test Case {i}:")
        print(f"Input: {arr}")
        print(f"Expected Output: {expected}")
        print(f"Your Output: {result}")
        print(f"{'✅ Passed' if result == expected else '❌ Failed'}\n")


if __name__ == '__main__':
    run_tests()
