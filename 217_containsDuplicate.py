#Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        countSet = set()
        for i in range(len(nums)):
            if nums[i] in countSet:
                return True
            else:
                countSet.add(nums[i])
        return False