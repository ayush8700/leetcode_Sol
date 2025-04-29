class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m=len(needle)
        n=len(haystack)
        if needle in haystack:
            for i in range(n):
                if needle in haystack[i:i+m]:
                    return i
                    break
        else:
            return -1
