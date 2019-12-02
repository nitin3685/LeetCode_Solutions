class Solution:
    def dist(self, a, b):
        dx, dy = a[0] - b[0], a[1] - b[1]
        if dx < 0:
            dx = -dx
        if dy < 0:
            dy = -dy
        return max(dx, dy)
    
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        return sum(self.dist(points[i - 1], points[i]) for i in range(1, len(points)))
