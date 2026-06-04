class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        lst = []
        for i in range(len(nums1)):
            lst.append(nums1[i])
        for j in range(len(nums2)):
            lst.append(nums2[j])
        lst.sort()
        n = len(lst)
        if n%2==0:
            return (lst[int(n/2)]+lst[int(n/2)-1])/2

        return lst[int(n/2)]
