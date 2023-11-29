class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rowCount = defaultdict(int)
        count = 0
        for row in grid:
            rowCount[tuple(row)] += 1
        for column in zip(*grid):
            count += rowCount[column]
        return count