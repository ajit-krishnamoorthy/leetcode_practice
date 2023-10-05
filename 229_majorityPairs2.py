class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        numDict = Counter(nums)
        countN = int(len(nums)/3)
        returnList = []
        return [x for x, count in numDict.items() if count > len(nums)//3]