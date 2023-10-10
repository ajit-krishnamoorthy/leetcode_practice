## array only of int, can be empty, 
## return true if all elements are unique, else return false, in boolean
## [2, 6, 97, 46, 55] -> True
## [33, 55, 27, 89, 55] -> False
## [] -> True
from collections import defaultdict 
def uniqueOccurences(self, arr: list[int]) -> bool:
    if len(arr) == 0:
        return True
    occurDict = defaultdict(int)
    for i in range(len(arr)):
        if occurDict[arr[i]] > 0:
            occurDict[arr[i]] += 1
        else:
            occurDict[arr[i]] = 1
    for i in range(len(arr)):
        if occurDict[arr[i]] > 1:
            return False
    return True


s = uniqueOccurences("", [2, 6, 97, 46, 55])
print(s)
print("True")
t = uniqueOccurences("", [33, 55, 27, 89, 55])
print(t)
print("False")
u = uniqueOccurences("", [])
print(u)
print("True")