class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        counter = defaultdict(int)
        for x in arr:
            counter[x] += 1
        for x in counter:
            if counter[x] > len(arr) // 4:
                return x