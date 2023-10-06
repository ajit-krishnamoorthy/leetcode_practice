class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandies = max(candies)
        listReturn = []
        for x in candies:
            if x + extraCandies >= maxCandies:
                listReturn.append(True)
            else:
                listReturn.append(False)
        return listReturn