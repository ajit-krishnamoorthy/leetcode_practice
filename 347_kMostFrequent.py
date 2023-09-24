    #Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        countDict = {}
        freq = [[] for i in range(len(nums)+1)]

        for n in nums:
            countDict[n] = 1 + countDict.get(n, 0)
        for n, c in countDict.items():
            freq[c].append(n)
        res = []
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res