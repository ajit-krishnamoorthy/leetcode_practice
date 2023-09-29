#Write an algorithm to determine if a number n is happy.
class Solution:
    def isHappy(self, n: int) -> bool:

        def recHappy(self, n: int) -> int:
            sum = 0
            while n > 0:
                digit = n % 10
                sum += digit*digit
                n = n // 10
            return sum
        
        visitSet = set()
        newSum = recHappy(self, n)
        if newSum == 1:
            return True
        visitSet.add(newSum)
        while newSum !=1:
            newSum = recHappy(self, newSum)
            if newSum in visitSet:
                return False
            visitSet.add(newSum)
        return True