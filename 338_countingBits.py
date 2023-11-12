class Solution:
    def countBits(self, n: int) -> List[int]:
        countList = []
        for x in range(n+1):
            binaryN = bin(x)[2:]
            countOfOne = binaryN.count('1')
            countList.append(countOfOne)
        return countList