class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        source_cities = set()
        destination_cities = set()
        for x in paths:
            if x[0] not in source_cities:
                source_cities.add(x[0])
            if x[1] not in destination_cities:
                destination_cities.add(x[1])
        return (destination_cities - source_cities).pop()
