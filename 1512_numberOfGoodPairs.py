class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        pairCount = 0
        seen = {}
        for x in nums:
            if x in seen:
                if seen[x] == 1:
                    pairCount += 1
                else:
                    pairCount += seen[x]
                seen[x] += 1
            else:
                seen[x] = 1
        return pairCount