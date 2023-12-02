class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        left = 0
        for right in range(len(s)):
            count[s[right]] = 1 + count.get(s[right], 0)
            windowSize = right-left+1
            if windowSize - max(count.values()) <= k:
                res = max(res, right-left+1)
            else:
                count[s[left]] -= 1
                left += 1
        return res