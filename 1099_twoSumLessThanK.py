class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        maxSum = -1
        nums.sort()
        left = 0
        right = len(nums) - 1
        while left < right:
            tempSum = nums[left] + nums[right]
            if tempSum < k:
                maxSum = max(maxSum, tempSum)
                left += 1
            else:
                right -= 1
        return maxSum
