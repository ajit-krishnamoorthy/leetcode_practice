class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0]*len(temperatures)
        stck = []
        for i, t in enumerate(temperatures):
            while stck and t > stck[-1][0]:
                stckTemp, stckIndex = stck.pop()
                answer[stckIndex] = i - stckIndex
            stck.append((t, i))
        return answer