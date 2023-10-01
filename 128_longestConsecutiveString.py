#Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.In O(n) time
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setNums = set(nums)
        countCons = 0
        for x in nums:
            if (x-1) not in setNums:
                length = 0
                while (x+length) in setNums:
                    length += 1
                if length > countCons:
                    countCons = length
        return countCons