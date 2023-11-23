class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        minNum = arrays[0][0]
        maxNum = arrays[0][-1]
        distance = 0
        for x in arrays[1:]:
            initialNum = x[0]
            finalNum = x[-1]
            distance = max(distance, maxNum - initialNum, finalNum - minNum)
            minNum = min(minNum, initialNum)
            maxNum = max(maxNum, finalNum)
        return distance