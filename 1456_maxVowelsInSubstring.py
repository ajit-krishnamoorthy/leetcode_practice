class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        firstIndex = 0
        lastIndex = k-1
        maxCount = 0
        for i in range(0, k):
            if s[i] in "aeiou":
                maxCount += 1
        currentCount = maxCount
        while lastIndex < len(s)-1:
            firstLetter = s[firstIndex]
            nextLetter = s[lastIndex+1]
            if firstLetter not in "aeiou" and nextLetter in "aeiou":
                currentCount += 1
            if firstLetter in "aeiou" and nextLetter not in "aeiou":
                currentCount -= 1
            if currentCount > maxCount:
                maxCount = currentCount
            firstIndex += 1
            lastIndex += 1
        return maxCount