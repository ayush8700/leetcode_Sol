class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        lst=list()
        lst=nums1+nums2
        lst.sort()
        a=len(lst)
        if(a%2==0):
            c=lst[int(a/2)]+lst[int(a/2)-1]
            return(c/2)
        else:
            b=lst[(int(a/2))]
            return(float(b))
            