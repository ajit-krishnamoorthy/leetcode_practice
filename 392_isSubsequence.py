#Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sCount = tCount = 0
        while sCount < len(s) and tCount < len(t):
            if s[sCount] == t[tCount]:
                sCount += 1
            tCount += 1
        return sCount == len(s)