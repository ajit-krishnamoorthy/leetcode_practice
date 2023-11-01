class Solution:
    def guessNumber(self, n: int) -> int:
        left = 1
        right = n
        while left <= right:
            mid = (left+right)//2
            count = guess(mid)
            if count == 0:
                return mid
            elif count == -1:
                right = mid -1
            else:
                left = mid+1