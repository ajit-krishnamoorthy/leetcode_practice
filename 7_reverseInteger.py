#Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

class Solution:
    def reverse(self, x: int) -> int:
        xStr = str(x)
        xStr = xStr[::-1]
        if xStr[-1] == '-':
             xStr = '-'+xStr[:-1]
        if xStr[0] == '0' and len(xStr) > 1:
            xStr = xStr[1:]
        if int(xStr) > pow(2, 31)-1 or int(xStr) < pow(-2, 31):
            return 0
        return int(xStr)