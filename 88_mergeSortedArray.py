class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nCount = n-1
        mCount = m-1
        totalCount = m+n-1
        while nCount >= 0:
            if mCount >= 0 and nums1[mCount] > nums2[nCount]:
                nums1[totalCount] = nums1[mCount]
                mCount -= 1
            else:
                nums1[totalCount] = nums2[nCount]
                nCount -= 1
            totalCount -= 1