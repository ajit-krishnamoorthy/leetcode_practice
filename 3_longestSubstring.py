#Given a string s, find the length of the longest substring without repeating characters.


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        leftPointer = 0
        res = 0
        subSet = set()
        for rightPointer in range(len(s)):
            while s[rightPointer] in subSet:
                subSet.remove(s[leftPointer])
                leftPointer +=1
            subSet.add(s[rightPointer])
            res = max(res, len(subSet))
        return res