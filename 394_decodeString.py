class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curString = ''
        curNum = 0
        for x in s:
            if x.isdigit():
                curNum = curNum*10 + int(x)
            elif x == '[':
                stack.append(curNum)
                stack.append(curString)
                curNum = 0
                curString = ''
            elif x == ']':
                tempString = stack.pop()
                tempNum = stack.pop()
                curString = tempString + curString*tempNum
            else:
                curString += x
        return curString
    