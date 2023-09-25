#Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        leftPointer = total = 0
        result = maxsize
        for rightPointer in range(len(nums)):
            total += nums[rightPointer]
            while total >= target:
                result = min(result, rightPointer-leftPointer+1)
                total -= nums[leftPointer]
                leftPointer += 1
        if result != maxsize:
            return result
        else:
            return 0