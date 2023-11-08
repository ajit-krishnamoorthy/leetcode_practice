class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = right = 0
        flip = 1
        maxCount = currCount = 0
        while right < len(nums):
            if nums[right] == 0:
                flip -= 1
            if flip < 0:
                if nums[left] == 0:
                    flip += 1
                left += 1
            if currCount > maxCount:
                maxCount = currCount
            right += 1
        return right - left -1