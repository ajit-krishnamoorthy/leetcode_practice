class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        retList = []
        nums.sort()
        
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue
            l = i+1
            r = len(nums) - 1
            while l < r:
                threeSum = nums[l] + nums[r] + a
                if threeSum == 0:
                    retList.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
                elif threeSum < 0:
                    l += 1
                elif threeSum > 0:
                    r -= 1
        return retList