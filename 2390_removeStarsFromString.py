class Solution:
    def removeStars(self, s: str) -> str:
        s2 = []
        for x in s:
            if x != "*":
                s2.append(x)
            if x == "*":
                s2.pop()
        return ''.join(s2)