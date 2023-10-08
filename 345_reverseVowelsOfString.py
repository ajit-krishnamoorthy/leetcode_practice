class Solution:
    def reverseVowels(self, s: str) -> str:
        left = 0
        right = len(s) - 1
        sList = list(s)
        while right > left:
            if sList[left] in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U') and sList[right] in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'):
                sList[left], sList[right] = sList[right], sList[left]
                right -= 1
                left += 1
            elif sList[left] in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U') and sList[right] not in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'):
                right -= 1
            elif sList[left] not in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U') and sList[right] in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'):
                left += 1
            else:
                left += 1
                right -= 1
        s = ''.join(sList)
        return s