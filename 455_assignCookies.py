class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        index = count = 0

        while index < len(s) and count < len(g):
            if s[index] >= g[count]:
                count += 1
            index += 1
        return count
