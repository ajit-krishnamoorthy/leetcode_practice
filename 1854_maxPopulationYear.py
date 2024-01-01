class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        d = defaultdict(int)

        for yearBirth, yearDeath in logs:
            for y in range(yearBirth, yearDeath):
                d[y] += 1
        maxYear = max(d.values())
        return min([i for i in d if d[i] == maxYear])
