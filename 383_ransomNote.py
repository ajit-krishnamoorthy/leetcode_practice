class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magDict = defaultdict(int)
        for x in magazine:
            magDict[x] += 1
        for x in ransomNote:
            if x not in magDict or magDict[x] < 1:
                return False
            magDict[x] -= 1
        return True