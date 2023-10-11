## two integer arrays, and we have to return an array which has two numbers, one with the distinct numbers in 1st array and second distinct elements in the second array
#integer arrays, different sizes, can also be empty
#[unique1, unique2]
## [1, 2, 4], [2, 6, 9] -> [[1, 4], [6, 9]]
## [24, 67, 2, 40, 3, 6], [24, 3, 6, 67, 33] -> [[2, 40], [33]]
## [1, 2, 4], [1, 2, 4] -> [[], []]

#Create two hashmaps, and store the arrays in the respective hash map as the keys
#Loop through each array, and check if the elements exist in hash map
#If they they are not present, then append it to the results array

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        num1L = num2L = []
        num1L = set(nums1) - set(nums2)
        num2L = set(nums2) - set(nums1)
        return [num1L, num2L]