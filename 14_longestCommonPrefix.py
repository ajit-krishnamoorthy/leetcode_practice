#Write a function to find the longest common prefix string amongst an array of strings.
#If there is no common prefix, return an empty string "".
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        commonPrefixCount = len(strs[0])
        for m in range(len(strs)-1):
            inner_count = 0 
            for n in range(0, min(len(strs[m]), len(strs[m+1]))):
                if strs[m][n] != strs[m+1][n]:
                    break
                else:
                    inner_count += 1
            if inner_count < commonPrefixCount:
                commonPrefixCount = inner_count
        return strs[0][0:commonPrefixCount]