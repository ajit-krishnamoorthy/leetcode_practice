#Given two strings s and t, return true if t is an anagram of s, and false otherwise.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countDict = defaultdict(int)
        for x in s:
            countDict[x] += 1
        for x in t:
            countDict[x] -= 1
        for i in countDict.values():
            if i != 0:
                return False
        return True