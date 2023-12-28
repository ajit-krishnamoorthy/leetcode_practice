class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        left = right = maxLength = 0
        hashMap = {}
        while right < len(s):
            hashMap[s[right]] = right
            if len(hashMap) > 2:
                minValue = min(hashMap.values())
                left = minValue + 1
                del hashMap[s[minValue]]
            maxLength = max(maxLength, right - left + 1)
            right += 1
        return maxLength
