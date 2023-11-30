class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles) == 1:
            return math.ceil(piles[0] / h)
        left = 0
        right = max(piles)
        minInt = max(piles)
        while left <= right:
            mid = (left+right) // 2
            if mid == 0:
                break
            count = 0
            for x in piles:
                count += math.ceil(x / mid)
            if count <= h and mid <= minInt:
                minInt = mid
                right = mid - 1
            elif count > h:
                left = mid + 1
            elif count < h:
                right = mid - 1
        return minInt