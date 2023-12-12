class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        largest = 0
        secondLargest = 0
        temp = 0
        for x in nums:
            if x > largest:
                secondLargest = largest
                largest = x
            elif x > secondLargest:
                secondLargest = x
        print(largest)
        print(secondLargest)
        return (largest-1)*(secondLargest-1)