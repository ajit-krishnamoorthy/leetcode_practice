#Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

#We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

#You must solve this problem without using the library's sort function.

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        leftPointer = 0
        rightPointer = len(nums)-1
        i = 0
        while i <= rightPointer:
            if nums[i] == 0:
                nums[i], nums[leftPointer] = nums[leftPointer], nums[i]
                leftPointer += 1
                i +=1
            elif nums[i] == 2:
                nums[i], nums[rightPointer] = nums[rightPointer], nums[i]
                rightPointer -= 1
            else:
                i += 1