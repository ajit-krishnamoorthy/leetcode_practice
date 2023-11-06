class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        if k==1:
            return max(arr[0], arr[1])
        if k > len(arr):
            return max(arr)
        currMax = arr[0]
        currWin = 0
        for i in range(1, len(arr)):
            if currMax > arr[i]:
                currWin += 1
            else:
                currMax = arr[i]
                currWin = 1
            if currWin == k:
                return currMax
        return currMax