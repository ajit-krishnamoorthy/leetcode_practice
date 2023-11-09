class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        numsDict = Counter(nums)
        count = 0
        for x in nums:
            if numsDict[x] > 0:
                numsDict[x] -= 1
                compliment = k - x
                if compliment in numsDict and numsDict[compliment] > 0:
                    numsDict[compliment] -= 1
                    count += 1
                else:
                    numsDict[x] += 1
        return count