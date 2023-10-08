class Solution:
    def reverseWords(self, s: str) -> str:
        sList = s.split()
        left = 0
        right = len(sList) - 1
        while right > left:
            sList[left], sList[right] = sList[right], sList[left]
            left += 1
            right -= 1
        s = " ".join(sList)
        return s