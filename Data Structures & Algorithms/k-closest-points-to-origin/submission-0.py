from math import sqrt
import heapq

class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.distance = sqrt(x**2 + y**2)

    def __lt__(self, other: Point):
        return self.distance < other.distance

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = [Point(x,y) for x,y in points]
        heapq.heapify(distances)
        result = []
        for _ in range(k):
            point = heapq.heappop(distances)
            result.append([point.x, point.y])
        return result