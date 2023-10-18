#String, only contains brackets, every open bracket has to be closed immediately after

#'{}()[][]' -> True
#'[]{}' -> True
#'' -> False
#'(]' -> False

def Paranthesis(self, s:str) -> bool:
    ## Create a hashmap with the brackets
    ## Loop through the string and create a stack of the bracket characters from the string
    ##Pop the most recent element of the stack and check if the most recent character of the string is the equivalent bracket from the stack
    brackets = {'{':'}', '(':')', '[':']'}
    stackBracket = []
    for x in s:
        if x in brackets:
            stackBracket.append(x)
        elif len(stackBracket) == 0 or x != brackets[stackBracket.pop()]:
            return False
    return len(stackBracket) == 0

print(Paranthesis("", '{}()[][]'))
print('True')
print(Paranthesis("", '[]{}'))
print('True')
print(Paranthesis("", ''))
print('False')
print(Paranthesis("", '(]'))
print('False')