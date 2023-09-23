#Given a string s consisting of words and spaces, return the length of the last word in the string.
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        sList = s.split()
        lastWord = sList[-1]
        return len(lastWord)