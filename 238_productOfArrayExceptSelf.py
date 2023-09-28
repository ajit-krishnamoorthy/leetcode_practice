#Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        res = [1]*length
        prefix = postfix = 1
        for i in range(length):
            res[i] = prefix
            prefix *= nums[i]
        for i in range(length-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res