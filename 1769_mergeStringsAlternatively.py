class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        newWord = ""
        index1 = 0
        index2 = 0
        for i in range(len(word1)+len(word2)):
            if i %2 == 0:
                if index1 < len(word1):
                    newWord += word1[index1]
                    index1 += 1
                else:
                    newWord += word2[index2]
                    index2 += 1  
            else:
                if index2 < len(word2):
                    newWord += word2[index2]
                    index2 += 1  
                else:
                    newWord += word1[index1]
                    index1 += 1                                 
        return newWord