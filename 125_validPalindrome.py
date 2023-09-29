#A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
class Solution:
    def isPalindrome(self, s: str) -> bool:
        newS = [x for x in s.lower() if x.isalnum()]
        return newS == newS[::-1]