class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        if not points or len(points) == 1:
            return 0
        time = 0
        for index,cur_point in enumerate(points):
            if index == len(points) - 1:
                return time
            next_point = points[index+1]
            cross_path = min(abs(cur_point[0] - next_point[0]),abs(cur_point[1] - next_point[1]))
            straight_path = max(abs(cur_point[0] - next_point[0]),abs(cur_point[1] - next_point[1])) - cross_path
            time += cross_path +straight_path
            
        
